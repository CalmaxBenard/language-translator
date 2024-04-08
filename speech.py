# Imports
import speech_recognition as sr
import os
from tkinter import messagebox
from gtts import gTTS
from translator import LanguageTranslator


class SpeechTranslator(LanguageTranslator):
    def __init__(self, root):
        super().__init__(root)
        self.recognize = sr.Recognizer()
        self.mc = sr.Microphone()

    def capture_voice(self):
        with self.mc as source:
            messagebox.showinfo("Start Key", "Say hello to start translation.")
            os.environ[
                "GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\pc\Downloads\cool-monolith-419708-7db501814ea0.json"
            self.recognize.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognize.listen(source=source)
            my_text = self.recognize.recognize_google_cloud(audio)
            my_text = my_text.lower()
