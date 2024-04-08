from tkinter import *
from translator import LanguageTranslator
from speech import SpeechTranslator


def main():
    root = Tk()
    app = LanguageTranslator(root)
    root.mainloop()

    translator = SpeechTranslator()
    translator.capture_and_translate()


if __name__ == "__main__":
    main()
