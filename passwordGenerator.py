from tkinter import *
import random
import string
import pyperclip

# Initialize tkinter
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")

# Header & Footer
Label(root, text="PASSWORD GENERATOR", font="arial 15 bold").pack()
Label(root, text="Create Random & Customized Password",
      font="arial 12 bold").pack(side=BOTTOM)

# Input password length
pass_label = Label(root, text="PASSWORD LENGTH",
                   font="arial 12 bold", fg="firebrick2").place(x=125, y=50)
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len,
                 width=10, font="10", bg="peach puff").place(x=150, y=90)

# Generate password
pass_str = StringVar()


def pass_generator():
    password = ""

    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(
            string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)

    for y in range(pass_len.get()-4):
        password = password + \
            random.choice(string.ascii_uppercase +
                          string.ascii_uppercase + string.digits + string.punctuation)

    pass_str.set(password)

# Copy password


def copy_password():
    pyperclip.copy(pass_str.get())
    Label(root, text="PASSWORD COPIED", font="arial 15 bold",
          fg="green").place(x=120, y=290)


# Buttons
Button(root, text="GENERATE PASSWORD", font="arial 11 bold", bg="LightCyan3",
       command=pass_generator).place(x=120, y=140)
Entry(root, textvariable=pass_str, font="10",
      bg="peach puff").place(x=125, y=190)

Button(root, text="COPY TO CLIPBOARD", font="arial 11 bold", bg="LightCyan3",
       command=copy_password).place(x=125, y=240)

root.mainloop()
