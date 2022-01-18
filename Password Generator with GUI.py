from tkinter import *
import string
import random

password_chars = string.ascii_letters + string.digits + string.punctuation

def password_generator():
    password_field.delete(0, END)
    length = int(char_input.get())
    password = "".join([random.choice(password_chars) for _ in range(length)])
    password_field.insert(0, password)

window = Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50, bg = "#1c5ad6")

label_title = Label(text = "Password Generator",
                    bg = "#1c5ad6",
                    fg = "#1cd6d0",
                    font=("Arial", 35, "bold"))
label_title.grid(row = 0, column = 0, columnspan = 3, pady = 30)

label_before_input = Label(text="I want a password with",
                           bg="#1c5ad6",
                           fg="#1cd6d0",
                           font=("Arial", 15, "bold"))
label_before_input.grid(row = 1, column = 0)

char_input = Entry(bg = "#1cd6d0")
char_input.grid(row = 1, column = 1)
char_input.insert(0, "12")
char_input.focus()

label_after_input = Label(text = "characters.",
                          bg = "#1c5ad6",
                          fg = "#1cd6d0",
                          font = ("Arial", 15, "bold"))
label_after_input.grid(row = 1, column = 2)

generate_password_button = Button(text = "Generate Password",
                                  bg = "#1cd6d0",
                                  height = 4,
                                  width = 55,
                                  command = password_generator)
generate_password_button.grid(row = 2, column = 0, columnspan = 3, padx = 50, pady = 50)

password_field = Entry(bg = "#1c5ad6",
                       font = ("Arial", 15, "bold"), width = 40)
password_field.grid(row = 3, column = 0, columnspan = 3)

window.mainloop()

