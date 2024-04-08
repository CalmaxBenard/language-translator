import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os


class SpeechTranslator:
    def __init__(self):
        self.recognizer = spr.Recognizer()
        self.mc = spr.Microphone()

    def capture_and_translate(self):
        with self.mc as source:
            print("Speak 'hello' to initiate the Translation!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            os.environ[
                "GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\pc\Downloads\cool-monolith-419708-7db501814ea0.json"
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.recognizer.listen(source)
            my_text = self.recognizer.recognize_google_cloud(audio)
            my_text = my_text.lower()

            if "hello" in my_text:
                translator = Translator()
                from_lang = "en"
                to_lang = "sw"

                print("Speak a sentence...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.recognizer.listen(source)
                get_sentence = self.recognizer.recognize_google_cloud(audio)

                try:
                    print(f"Phrase to be translated \n{get_sentence}")
                    text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
                    text = text_to_translate.text

                    speak = gTTS(text=text, lang=to_lang, slow=False)
                    speak.save("captured_voice.mp3")
                    os.system("start captured_voice.mp3")
                except spr.UnknownValueError:
                    print("Unable to understand the input")
                except spr.RequestError as e:
                    print(f"Unable to provide required output {e}.")


