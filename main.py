import random
from tkinter import *
from tkinter import messagebox
import pyperclip as py
import json

FONT = "Arial"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    pass_entry.delete(0, END)

    password_letters = [random.choice(LETTERS) for char in range(random.randint(8,10))]
    password_symbols = [random.choice(SYMBOLS) for char in range(random.randint(2,4))]
    password_num = [random.choice(NUMBERS) for char in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_num
    random.shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(0, password)
    py.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    new_data = {
        web_entry.get(): {
            "email": email_entry.get(),
            "password": pass_entry.get(),
            }
    }

    if len(web_entry.get()) == 0 or len(email_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Please make sure to not leave any fields empty.")

    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- LOAD DATA ------------------------------- #

def load_data():
    with open("data.json", mode="r") as file:
        data = json.load(file)

        if web_entry.get() in data:
            email_entry.delete(0, END)
            pass_entry.delete(0, END)

            email_entry.insert(0, data[web_entry.get()]["email"])
            pass_entry.insert(0, data[web_entry.get()]["password"])

        else:
            messagebox.showerror(title="Error", message="Data not found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#Image
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", font=(FONT, 10, "normal"))
website_label.grid(column=0, row=1, sticky="e")

email_label = Label(text="Email/Username:", font=(FONT, 10, "normal"))
email_label.grid(column=0, row=2, sticky="e")

password_label = Label(text="Password:", font=(FONT, 10, "normal"))
password_label.grid(column=0, row=3, sticky="e")

#Entries
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "example@email.com")

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3, sticky="w")

#Buttons
generate_bt = Button(text="Generate Password", width=15, command=generate_password)
generate_bt.grid(column=2, row=3, sticky="e")
add_bt = Button(text="Add Data", width=46, command=save_password)
add_bt.grid(column=1, row=4, columnspan=2, sticky="w")
load_bt = Button(text="Load Data", width=15, command=load_data)
load_bt.grid(column=2, row=2, sticky="e")


window.mainloop()