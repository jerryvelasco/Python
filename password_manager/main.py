from tkinter import *
from tkinter import messagebox
import random
import pyperclip

"""searches for passwords in json file"""
def find_pw():
    website = website_input.get().capitalize()

    #tries opening file
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="File Doesn't exist", message="No Data File Found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")

        else:
            #prompts message if website doesnt exist
            messagebox.showerror(title="Error", message=f"No details for {website} exist.")



"""creates random password with symbols, letters and numbers"""
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #password length 
    num_of_letters = random.randint(8,10)
    num_of_symbols = random.randint(2,4)
    num_of_numbers = random.randint(2,4)

    #based on the random num generated loops through lists and grabs random items 
    random_letters = [random.choice(letters) for _ in range(num_of_letters)]
    random_symbols = [random.choice(symbols) for _ in range(num_of_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(num_of_numbers)]

    password_list = random_letters + random_numbers + random_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, string=f"{password}")
    pyperclip.copy(password)



"""remove label"""
def remove_label():
    result_label.config(text="")



"""save data entries to a text file"""
def save_data():

    #grabs input values
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    #creates new dictionary for json file
    website_dictionary = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }
    
    #makes sure inputs arent empty
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="empty fields", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                read_data = json.load(file)
                
        #creates new json file using inputs if it doesnt exist 
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            #write new inputs to json file
            read_data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(read_data, file, indent=4) 

        finally:
            #removes text from fields after writing them to the txt file
            website_input.delete(first=0, last=END)
            email_input.delete(first=0, last=END)
            password_input.delete(first=0, last=END)
    
            result_label.config(text="Succesfully Added!", fg="green")
            result_label.after(5000, remove_label)     #removes label after 5secs 
            website_input.focus()                      #moves cursor to website input box



"""UI setup"""
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
search_button = Button(text="Search", width=11, command=find_pw)
search_button.grid(column=2, row=1)

generate_pw_button = Button(text="Generate Password", width=11, command=generate_pw)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
