from tkinter import *
FONT = "Cambria"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    with open("data.txt", mode="a") as file:
        file.write(f"{web_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n")

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
generate_bt = Button(text="Generate Password", width=15)
generate_bt.grid(column=2, row=3, sticky="e")
add_bt = Button(text="Add", width=46, command=save_password)
add_bt.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()