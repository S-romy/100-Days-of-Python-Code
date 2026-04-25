from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Generate random letter(s) using the user input
def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    l_password = [random.choice(letters) for _ in range(random.randint(8, 10))]
    s_password = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    n_password = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = l_password + s_password + n_password

    # Shuffle the password
    random.shuffle(password_list)

    # Convert password from list to string
    shuffled_password = ''.join(password_list)

    if password_entry.get():
        if messagebox.askyesno(title=website_entry.get(),
                               message=f"Do you want to generate another password?: {password_entry.get()}"):
            password_entry.delete(0, END)
            password_entry.insert(0, shuffled_password)
    else:
        password_entry.insert(END, shuffled_password)


# ---------------------------- DETECT USER PASSWORD STRENGTH ------------------------------- #
def check_password(user_password):
    strength = 0
    if len(user_password) >= 8:
        strength += 1
    if any(char.isupper() for char in user_password):
        strength += 1
    if any(char.islower() for char in user_password):
        strength += 1
    if any(char.isdigit() for char in user_password):
        strength += 1
    if any(char in ["!", "#", "$", "%", "&", "(", ")", "*", "+"] for char in user_password):
        strength += 1
    return strength


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email_or_password = email_or_username_entry.get()
    password = password_entry.get()

    if website and email_or_password and password:
        # Blocks weak passwords
        if check_password(password) < 4:
            messagebox.showwarning(title=website, message="Your password is weak, Please change it or"
                                                          f" generate one automatically. \nPassword: {password}")
            password_entry.delete(0, END)
        # Only strong passwords get through
        else:
            if messagebox.askokcancel(title=website, message="These are the details entered. \nEmail/Password: "
                                                             f"{email_or_password}\nPassword: {password}"
                                                             " \nIs it ok to save?"):
                with open("password_manager.txt", mode="a") as password_manager:
                    password_manager.write(f"{website} | {email_or_password} | {password}\n")
                    pyperclip.copy(password)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:", font=("Arial", 12, "normal"))
website_label.grid(column=0, row=1)

email_or_username_label = Label(text="Email/Username:", font=("Arial", 12, "normal"))
email_or_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 12, "normal"))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_or_username_entry = Entry(width=35)
email_or_username_entry.insert(0, "orahachi16@gmail.com")
email_or_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
