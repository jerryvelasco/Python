from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_pw(): 

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_of_letters = random.randint(8,10)
    num_of_symbols = random.randint(2,4)
    num_of_numbers = random.randint(2,4)

    #new_list = [new_item for item in list]
    random_letters = [random.choice(letters) for _ in range(num_of_letters)]
    random_symbols = [random.choice(symbols) for _ in range(num_of_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(num_of_numbers)]

    password_list = random_letters + random_symbols + random_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, string=f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_inputs():
    result_label.config(text="")
    

def save():
    
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="empty fields", message="Please don't leave any fields empty.")
    
    else: 
        isOk = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail: {email_data} \nPassword: {password_data} \nIs it ok to save?")

        if isOk:

            with open("data.txt", "a") as file:
                file.write(f"{website_data} | {email_data} | {password_data}\n")
        
                website_input.delete(first=0, last=END)
                email_input.delete(first=0, last=END)
                password_input.delete(first=0, last=END)

            result_label.config(text="Succesully Added!", fg="green")
            result_label.after(5000, clear_inputs)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


#labels 
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

result_label = Label(text="")
result_label.grid(column=0, row=4)


#inputs
website_input = Entry(width=36)
# website_input.insert(0, string="Enter a website")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=36)
# email_input.insert(0, string="Enter your email/username")
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)


#buttons 
generate_pw_button = Button(text="Generate Password", width=11, command=generate_random_pw)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()


