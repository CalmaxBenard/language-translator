# Import libraries
from tkinter import *
from tkinter import messagebox, ttk
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

# Define text boxes
text_input = Text(frame, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_input.place(x=10, y=100)

text_output = Text(frame, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_output.place(x=300, y=100)

# Define control buttons
btn1 = Button(frame, text="Translate", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"),
              bg="#248aa2", fg="white", cursor="hand2")
btn1.place(x=185, y=300)


root.mainloop()


