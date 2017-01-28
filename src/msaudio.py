import speech_recognition as sr
import os
import dirconf


def translate(AUDIO_FILE):
    # AUDIO_FILE = os.path.join(dirconf.AUDIO, 'out.wav')

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    BING_KEY = "54b20e711d4243fea1472c2d6cb33b78"

    try:
        return r.recognize_bing(audio, key=BING_KEY)
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))


def translate_all():
    text_segments = []
    for audiofile in os.listdir(dirconf.AUDIO):
        if audiofile.endswith('.wav'):
            file = os.path.join(dirconf.AUDIO, audiofile)
            print file
            text_segments.append(translate(file))
    return text_segments
