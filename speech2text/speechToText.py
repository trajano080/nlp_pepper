from vosk import Model, KaldiRecognizer, SetLogLevel
import wave

def speech_to_text(filename):

    SetLogLevel(0)
    model = Model("speech2text/model")

    wf = wave.open(filename)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    string = rec.PartialResult()
    
    txt_filename = "textFile.txt"
    f = open(txt_filename,"w")

    f.write(string[17:len(string)-3])
    f.close()

    return txt_filename