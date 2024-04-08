# Import libraries
from tkinter import *
from tkinter import messagebox, ttk
from googletrans import Translator, LANGUAGES

# Screen setup
root = Tk()
root.title("Language Translator")
root.geometry("590x370")

# Style the screen
frame = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg="#F7DC6F")
frame.place(x=0, y=0)


# translate function
def translate():
    lang = text_input.get(1.0, "end")
    chosen_lang = choose_language.get()

    if lang == "":
        messagebox.showerror("Language Translator", "Enter the text to translate!")
    else:
        text_output.delete(1.0, "end")
        translator = Translator()
        output = translator.translate(lang, dest=chosen_lang)
        text_output.insert("end", output.text)


# clear function
def clear():
    text_input.delete(1.0, "end")
    text_output.delete(1.0, "end")


# Add selection mode for text entry
a = StringVar()
auto_select = ttk.Combobox(frame, width=27, textvariable=a, state="randomly", font=("verdana", 10, "bold"))
auto_select["values"] = "Auto Select"
auto_select.place(x=15, y=60)
auto_select.current(0)

# Add language selection method
language = StringVar()
choose_language = ttk.Combobox(frame, width=27, textvariable=language, state="randomly", font=("verdana", 10, "bold"))
choose_language["values"] = list(LANGUAGES.values())
choose_language.place(x=300, y=60)
choose_language.current(0)

# Set title/label on screen
Label(root, text="Language Translator", font=("Helvetica", 20, "bold"), fg="black", bg="#F7DC6F").pack(pady=10)

# Define text boxes
text_input = Text(frame, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_input.place(x=10, y=100)

text_output = Text(frame, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_output.place(x=300, y=100)

# Define control buttons
btn1 = Button(frame, command=translate, text="Translate", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"),
              bg="#248aa2", fg="white", cursor="hand2")
btn1.place(x=185, y=300)

btn2 = Button(frame, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"),
              bg="#248aa2", fg="white", cursor="hand2")
btn2.place(x=300, y=300)

root.mainloop()
