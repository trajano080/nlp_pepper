#!/user/bin/env python
#=====================================================================================================================#
#                                               SOUND PROCESSING MODULE                                               #
#=====================================================================================================================#
import time
import signal
from queue import Queue
import numpy
from std_msgs.msg import String
import rospy
import qi
import sys

from scipy.io import wavfile
from GPSRparser.Parser import Parser

from vosk import Model, KaldiRecognizer
import wave
from dialog_utils.utils import *
import os
from dialog_pepper.srv import *


def handler(signum, frame):
    exit(1)


signal.signal(signal.SIGINT, handler)


class VoskReco():
    def __init__(self):
        model_path = os.path.join(get_pkg_path(), "models/vosk_model/")
        self.model = Model(model_path)

    def speech_to_text(self, filename):
        wf = wave.open(filename)
        rec = KaldiRecognizer(self.model, wf.getframerate())
        rec.SetWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)

        string = rec.PartialResult()

        return string[17:len(string)-3]


class SpeechToIntentSrv():
    def __init__(self, app):
        app.start()
        session = app.session
        print("Connected to pepper session")
        self.parsing = Parser()
        self.module_name = "SpeechToIntentSrv"
        self.vosk_reco = VoskReco()

        #===================== Set ALAudioDevice =====================#
        self.ALAudioDevice = session.service("ALAudioDevice")
        self.ALAudioDevice.enableEnergyComputation()
        self.SampleRate = 48000
        self.Channels = 4
        #/////////////////////////////////////////////////////////////#

        #============= Speaker's recognition parameters ==============#
        self.rstCounterSpeech = 3  # number of iteration before starting recording
        self.rstCounterSilence = 8  # number of iteration before stoping recording

        self.counterSpeech = self.rstCounterSpeech
        self.counterSilence = self.rstCounterSilence

        self.timeOutInternalCounter = 140
        self.rstTimeOutInternalCounter = 140

        self.FrontMicImportance = 2.0       # Front Left
        self.LeftMicImportance = 0.25       # Rear Left
        self.RightMicImportance = 0.25      # Rear Right
        self.RearMicImportance = 2.0        # Front Right

        #=============== Lists to save the sound data ================#
        self.queueSize = 6
        self.previous_sound_data = Queue(self.queueSize)
        self.soundData = []
        self.micData = []
        self.status = "Silence"

        self.thOffset = 450
        self.threshold = 0
        self.hh = 0.8
        self.ll = 1 - self.hh

        self.recordingInProgress = False
        self.firstTime = True
        #/////////////////////////////////////////////////////////////#

        #=============== Lists to save the sound data ================#
        self.queueSize = 6
        self.previous_sound_data = Queue(self.queueSize)
        self.soundData = []
        self.micData = []

        self.no_sentence = True
        self.sentence = ""



    def intent_callback(self,req):
        print("Start Processing")
        try:
            self.sentence = ""
            self.ALAudioDevice.setClientPreferences(
                self.module_name, self.SampleRate, self.Channels, 0)
            self.ALAudioDevice.subscribe(self.module_name)
            print("subscribed")
            while self.no_sentence:
                pass
            self.ALAudioDevice.unsubscribe(self.module_name)
            print("unsubscribed")

            rospy.loginfo(B+"[Robobreizh - Dialog] Parsing intent..."+W)
            parser = Parser()
            parser_intent = parser.classifier(self.sentence)
            # reset variable for the next call
            self.no_sentence = True
            self.firstTime = True

            return ActionResponse(parser_intent)
        except Exception as e:
            raise e

    def start_sti_srv(self):
        rospy.init_node('sti_srv', anonymous=True)
        rospy.Service('/robobreizh/dialog_pepper/speech_to_intent', Action,self.intent_callback)
        rospy.loginfo(B+"[Robobreizh - Dialog] Speech to intent server started"+W)
        rospy.spin()


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def convert_str_to_int(self, data):
        signedData = []
        ind = 0

        for i in range(0, int(len(data)/2)):
            signedData.append(data[ind]+data[ind+1]*256)

            ind = ind + 2

        for i in range(0, int(len(signedData))):
            if signedData[i] >= 32768:
                signedData[i] = signedData[i]-65536

        for i in range(0, int(len(signedData))):
            signedData[i] = signedData[i]/32767.0

        return signedData

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def processRemote(self, nbOfChannels, nbOfSamplesByChannel, timeStamp, inputBuffer):

        #====== Audio stream callback method with simple silence detection =========#
        self.soundData = self.convert_str_to_int(inputBuffer)

        self.energy = (((self.ALAudioDevice.getFrontMicEnergy()*self.FrontMicImportance) +
                        (self.ALAudioDevice.getLeftMicEnergy()*self.LeftMicImportance) +
                        (self.ALAudioDevice.getRightMicEnergy()*self.RightMicImportance) +
                        (self.ALAudioDevice.getRearMicEnergy()*self.RearMicImportance))
                       / 4)

        #============================ First Iteration ==============================#
        if (self.firstTime):
            rospy.loginfo(B+"[Robobreizh - Dialog] Sound detection in progress ..."+W)
            self.ymin_prev = self.energy
            self.ymax_prev = self.energy
            self.ymed_prev = self.energy
            self.firstTime = False
        #///////////////////////////////////////////////////////////////////////////#

        if (self.energy > self.ymax_prev):
            self.ymax = self.energy
        else:
            self.ymax = self.hh * self.ymax_prev + self.ll * self.ymed_prev

        if (self.energy < self.ymin_prev):
            self.ymin = self.energy
        else:
            self.ymin = self.ll * self.ymin_prev + self.hh * self.ymed_prev

        self.ymed = (self.ymin + self.ymax) / 2

        #============================ Possible States ==============================#
        if (self.status == "Silence"):
            if (self.energy > self.ymed_prev + self.thOffset):
                self.status = "possibleSpeech"
                self.threshold = self.ymed_prev + self.thOffset
                self.counterSpeech = self.rstCounterSpeech - 1

        elif (self.status == "possibleSpeech"):
            print("possibleSpeech")
            self.counterSpeech -= 1
            if (self.energy > self.threshold and self.energy > self.ymed):
                if (self.counterSpeech <= 0):
                    self.counterSpeech = self.rstCounterSpeech
                    self.status = "Speech"
                    self.start_recording()
                    self.timeOutInternalCounter = self.rstTimeOutInternalCounter - self.rstCounterSpeech
                else:
                    self.status = "possibleSpeech"
            else:
                self.status = "Silence"

        elif (self.status == "Speech"):
            print("speech")
            if (self.energy < self.ymed and self.energy < self.threshold):
                self.status = "possibleSilence"
                self.threshold = self.ymed
                self.counterSilence = self.rstCounterSilence - 1
            else:
                self.status = "Speech"

        elif (self.status == "possibleSilence"):
            self.counterSilence -= 1
            if (self.energy > self.threshold):
                self.status = "Speech"
            elif (self.counterSilence == 0):
                self.status = "Silence"
                self.stop_recording()
            else:
                self.status = "possibleSilence"

        else:
            self.status = "Silence"

        #///////////////////////////////////////////////////////////////////////////#

        #=========== Way out in case of spending a lot of time listening ===========#
        if(self.status != "Silence"):
            self.timeOutInternalCounter -= 1

        if(self.timeOutInternalCounter == 0):
            self.status = "Time limit reached"
            self.timeOutInternalCounter = self.rstTimeOutInternalCounter
            self.recordingInProgress = False
            self.micData = []
            self.previous_sound_data = Queue(self.queueSize)
            print("SPEECH IS TAKING MORE TIME THAN EXPECTED")
            text = "Speech is taking more time than expected. Try again, i am listening"
            self.aLTextToSpeech.say(text)
            self.status = "Silence"
        #///////////////////////////////////////////////////////////////////////////#

        self.ymin_prev = self.ymin
        self.ymax_prev = self.ymax
        self.ymed_prev = self.ymed

        if self.recordingInProgress:
            self.micData += self.soundData
        else:
            if self.previous_sound_data.full():
                self.previous_sound_data.get()

            self.previous_sound_data.put(self.soundData)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def start_recording(self):
        #=================== Retrieve the previous buffer data =====================#
        self.recordingInProgress = True
        while not self.previous_sound_data.empty():
            self.micData += self.previous_sound_data.get()

        rospy.loginfo(B+"[Robobreizh - Dialog] Recording message..."+W)


    def stop_recording(self):
        rospy.loginfo(B+"[Robobreizh - Dialog] Stopping recording ..."+W)
        #==================== Saves the recording to memory ========================#

        wav_filename = "stereofile.wav"
        Data = self.float_to_pcm(self.micData, 'int16')
        wavfile.write(wav_filename, self.SampleRate, Data)

        #==================== Saves the recording to memory ========================#
        self.sentence = self.vosk_reco.speech_to_text(wav_filename)

        print("\n\n------------------------\n\n")
        print("Recognized text: " + self.sentence)

        self.recordingInProgress = False
        self.micData = []
        self.previous_sound_data = Queue(self.queueSize)
        self.no_sentence = False


    def stop_recording_QA(self):
        #==================== Saves the recording to memory ========================#
        print("Stopped Recording")

        #========================= wavfile creation ================================#
        initial_time = time.time()

        wav_filename = "stereofile.wav"
        Data = self.float_to_pcm(self.micData, 'int16')
        wavfile.write(wav_filename, self.SampleRate, Data)
        print("The wav file was created")

        duration = time.time() - initial_time
        print("\n==> This task took ", duration, "seconds\n")
        #///////////////////////////////////////////////////////////////////////////#

        #========================= txtfile creation ================================#
        initial_time = time.time()

        txt_filename = self.vosk_reco.speechToText.speech_to_text(wav_filename)
        print("The txt file was created")

        duration = time.time() - initial_time
        print("\n==> This task took ", duration, "seconds\n")
        #///////////////////////////////////////////////////////////////////////////#

        #====================== Question-Answer section ============================#
        initial_time = time.time()

        file = open(txt_filename)
        text = file.readline()
        file.close()
        nlp = NLPModule.NLPmodule()
        question = nlp.question_filter(text)

        if (type(question) == dict):
            answer = nlp.search(
                text, question["category"], question["question_search_doc"])
        else:
            answer = question

        print("\n===========================================")
        print("\nQuestion: {}".format(text))
        print("Answer: {}".format(answer))
        print("===========================================\n\n")

        self.aLTextToSpeech.say(answer)

        duration = time.time() - initial_time
        print("\n==> This task took ", duration, "seconds\n")
        #///////////////////////////////////////////////////////////////////////////#

        time.sleep(1.5)
        self.aLTextToSpeech.say("I am ready for another question")

        self.recordingInProgress = False
        self.micData = []
        self.previous_sound_data = Queue(self.queueSize)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def float_to_pcm(self, myrecording, dtype):
        myrecording = numpy.asarray(myrecording)
        i = numpy.iinfo(dtype)
        abs_max = 2 ** (i.bits - 1)
        offset = i.min + abs_max
        return (myrecording * abs_max + offset).clip(i.min, i.max).astype(dtype)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#



#=====================================================================================================================#
#                                                       MAIN                                                          #
#=====================================================================================================================#
if __name__ == "__main__":

    #======= Connection and Initialization of qi framework =======#
    try:
        # Initialize qi framework.
        connection_url = "tcp://127.0.0.1:9559"
        app = qi.Application(
            ["SpeechToIntentSrv", "--qi-url=" + connection_url])
    except RuntimeError:
        print(f"Can't connect to Naoqi {connection_url}")
        print("Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    #/////////////////////////////////////////////////////////////#

    #============= Running spekaker's recognition ===============#
    MySpeechToIntentSrv = SpeechToIntentSrv(app)
    app.session.registerService(
        "SpeechToIntentSrv", MySpeechToIntentSrv)
    MySpeechToIntentSrv.start_sti_srv()

    print("Disconnected")
#=====================================================================================================================#
#=====================================================================================================================#
