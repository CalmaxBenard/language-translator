# Import libraries
from tkinter import Tk, Frame, messagebox, ttk, RIDGE, Label, Text
from googletrans import Translator

# Screen setup
root = Tk()
root.title("Language Translator")
root.geometry("590x370")

# Style the screen
frame = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg="#F7DC6F")
frame.place(x=0, y=0)

# Set title/label on screen
Label(root, text="Language Translator", font=("Helvetica", 20, "bold"), fg="black", bg="#F7DC6F").pack(pady=10)

text_input = Text(frame, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_input.place(x=10, y=100)


root.mainloop()


