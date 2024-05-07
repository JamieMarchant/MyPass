from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, (password))
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_information():
    
    # Get data from entry fields
    website_get = website_entry.get()
    password_get = password_entry.get()
    email_get = email_usrname_entry.get()
    
    if len(website_get) == 0 or len(email_get) == 0 or len(password_get) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        # Confirm with user that information is correct
        is_ok = messagebox.askokcancel(title="Confirm Details", message=(f"These are the details entered: \nWebsite: {website_get} \nEmail: {email_get} \nPassword: {password_get} \nIs it ok to save?"))
    
        # Open the file in append mode and close it automatically after writing
        if is_ok:
            with open("data.txt", "a") as file:
                # Concatenate the data into a single string
                data_to_write = (f"{website_get} / {password_get} / {email_get}\n")
        
                # Write the data to the file
                file.write(data_to_write)
                # Clear the website and password entries
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_usrname_label = Label(text="Email/Username:")
email_usrname_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_usrname_entry = Entry(width=35)
email_usrname_entry.grid(row=2, column=1, columnspan=2)
email_usrname_entry.insert(0, "YourEmail@Email.com")

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=35, command=save_information, )
add_button.grid(row=4, column=1, columnspan=2)










































window.mainloop()
