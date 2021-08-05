from tkinter import *
from tkinter import messagebox
import random
import pyperclip  #for copying pw to clipboard

BG_COLOR = "#2c394b" # light green
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------- Lists needed for password generator ______________#
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # combine 3 lists into one so it can be shuffled
    password = password_symbols + password_numbers + password_letters
    random.shuffle(password)
    # convert list to a string
    password_string = "".join(password)
    entry_password.insert(0, password_string)
    pyperclip.copy(password_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    new_data = f"{entry_website.get()} | {entry_username.get()} | {entry_password.get()}\n"
    # have user approve of data using messagebox before writing to file
    if len(entry_website.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showinfo(title="Oops", message=f"You should not have any blank fields.\n\nPlease correct and try again")
    else:
        is_ok = messagebox.askokcancel(title="Confirm", message=f"Add this info?\n\n{new_data}")

        # a = append mode. Will create the file if it doesn't exist
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(new_data)
            entry_website.delete(0, END)
            entry_website.focus()
            entry_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

#Creating a new window and configurations
window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(padx=40, pady=40)

# canvas size based on image size
canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# labels
label_website = Label(text="Website: ")
label_website.config(padx=0, pady= 2, fg=BG_COLOR)
label_website.grid(column=0, row=1)

label_username = Label(text="Email/Username: ")
label_username.config(padx=0, pady= 2, fg=BG_COLOR)
label_username.grid(column=0, row=2)

label_password = Label(text="Password: ")
label_password.config(padx=0, pady= 2, fg=BG_COLOR)
label_password.grid(column=0, row=3)



# text input (entry)
#Entries
entry_website = Entry(width=50, justify="left")
print(entry_website.get())
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2)

entry_username = Entry(width=50)
print(entry_username.get())
entry_username.insert(0, "example@example.com")
entry_username.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=30)
print(entry_password.get())
entry_password.grid(column=1, row=3)

# buttons
button_generate_password = Button(text="Generate Password", command=generate)
button_generate_password.config(width=14, padx=0, pady= 2, fg=BG_COLOR)
button_generate_password.grid(column=2, row=3)

button_add_info = Button(text="Add", command=add)
button_add_info.config(width=44, padx=0, pady= 2, fg=BG_COLOR)
button_add_info.grid(column=1, row=4, columnspan=2)

window.mainloop()