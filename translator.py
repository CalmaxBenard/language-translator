from tkinter import *
from tkinter import messagebox, ttk
from googletrans import Translator, LANGUAGES


class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("590x370")

        self.frame = Frame(self.root, width=590, height=370, relief=RIDGE, borderwidth=5, bg="#F7DC6F")
        self.frame.place(x=0, y=0)

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="Language Translator", font=("Helvetica", 20, "bold"), fg="black", bg="#F7DC6F").pack(
            pady=10)

        self.text_input = Text(self.frame, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
        self.text_input.place(x=10, y=100)

        self.text_output = Text(self.frame, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
        self.text_output.place(x=300, y=100)

        self.auto_select = ttk.Combobox(self.frame, width=27, state="readonly", font=("verdana", 10, "bold"))
        self.auto_select["values"] = ("Auto Select",)
        self.auto_select.place(x=15, y=60)
        self.auto_select.current(0)

        self.choose_language = ttk.Combobox(self.frame, width=27, state="readonly", font=("verdana", 10, "bold"))
        self.choose_language["values"] = list(LANGUAGES.values())
        self.choose_language.place(x=300, y=60)
        self.choose_language.current(0)

        btn1 = Button(self.frame, command=self.translate, text="Translate", relief=RAISED, borderwidth=2,
                      font=("verdana", 10, "bold"), bg="#248aa2", fg="white", cursor="hand2")
        btn1.place(x=185, y=300)

        btn2 = Button(self.frame, command=self.clear, text="Clear", relief=RAISED, borderwidth=2,
                      font=("verdana", 10, "bold"), bg="#248aa2", fg="white", cursor="hand2")
        btn2.place(x=300, y=300)

    def translate(self):
        lang = self.text_input.get(1.0, "end")
        chosen_lang = self.choose_language.get()

        if lang.strip() == "":
            messagebox.showerror("Language Translator", "Enter the text to translate!")
        else:
            self.text_output.delete(1.0, "end")
            translator = Translator()
            output = translator.translate(lang, dest=chosen_lang)
            self.text_output.insert("end", output.text)

    def clear(self):
        self.text_input.delete(1.0, "end")
        self.text_output.delete(1.0, "end")
