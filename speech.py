# Imports
import speech_recognition as sr
from gtts import gTTS


class SpeechTranslator:
    def __init__(self):
        self.recognize = sr.Recognizer()
        self.mc = sr.Microphone()



