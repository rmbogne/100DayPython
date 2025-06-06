from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ------------ PASSWORD GENERATOR -------------------------------- #
#Password Generator Project

def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    fld_password.insert(0, password)
    pyperclip.copy(password)

# ------------ SAVE PASSWORD ------------------------------------- #
def savedata():
    website = fld_website.get()
    email = fld_username.get()
    passwd = fld_password.get()

    new_data = {
        website: {
            "email": email,
            "password": passwd
        }
    }
    if len(email) == 0 or len(passwd) == 0:
        messagebox.showwarning(title="Error", message="One or more fields are empty. Please provide the missing data")

    else:
        try:
            with open("data.json", "r") as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as f:
                # Saving new data
                json.dump(data, f, indent=4)
        finally:
            fld_website.delete(0, END)
            fld_password.delete(0,END)

# ------------ SEARCH PASSWORD ------------------------------------------ #
def find_password():
    website = fld_website.get()
    try:
        with (open("data.json", "r") as f):
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
                messagebox.showwarning(title="oops", message=f"{website} doesn't match our records")


# ------------ UI SETUP ------------------------------------------ #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
lbl_website = Label(text="WebSite:")
lbl_website.grid(row=1, column=0)

lbl_username = Label(text="Email/Username:")
lbl_username.grid(row=2, column=0)

lbl_password= Label(text="Password:")
lbl_password.grid(row=3, column=0)

# Fields
fld_website = Entry(width=21)
fld_website.grid(row=1, column=1)
fld_website.focus()

fld_username = Entry(width=37)
fld_username.grid(row=2, column=1, columnspan=2)
fld_username.insert(0,"example@example.com")

fld_password= Entry(width=21)
fld_password.grid(row=3, column=1)

#Buttons
btn_search = Button(text="Search", width=11, command=find_password)
btn_search.grid(row=1, column=2)

btn_genpwd = Button(text="Generate password", width=11, command=generate_passwd)
btn_genpwd.grid(row=3, column=2)

btn_adduser = Button(text="Add",width=35, command=savedata)
btn_adduser.grid(row=4, column=1, columnspan=2)


window.mainloop()
