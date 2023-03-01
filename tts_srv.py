import qi
import rospy
import sys
from dialog_pepper.srv import Msg
from dialog_utils.utils import *

class TTS():
    def __init__(self):
        self.first_time = True
        rospy.init_node('tts_srv', anonymous=True)
        session = qi.Session()
        try:
            session.connect("tcp://localhost:9559")
        except RuntimeError:
            print("Can't connect to Naoqi")
            sys.exit(1)

        #===================== Set ALTextToSpeech ====================#
        self.aLTextToSpeech = session.service("ALTextToSpeech")
        self.aLTextToSpeech.setLanguage("English")
        self.aLTextToSpeech.setParameter("volume", 100)
        self.aLTextToSpeech.setParameter("pitch", 100)
        self.aLTextToSpeech.setParameter("speed", 80)


        self.tts_srv = rospy.Service('/robobreizh/dialog_pepper/text_to_speech_srv', Msg, self.speakCb)

        rospy.loginfo(B+"[Robobreizh - Dialog] Text to speech server started"+W)
        rate = rospy.Rate(5)
        rospy.spin()

    def speakCb(self,req):
        self.aLTextToSpeech.say(req.sentence)
        return MsgResponse(True)

if __name__ == "__main__":
    tts = TTS()
