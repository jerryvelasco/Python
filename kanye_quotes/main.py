from tkinter import *
import requests

#documentation - https://kanye.rest

def get_quote():
    response = requests.get(url="https://api.kanye.rest")           #request data from api
    response.raise_for_status()                                     #raises exceptions for any possible json error codes
    quote = response.json()["quote"]                                #selects the quote text from the json dictionary
    canvas.itemconfig(quote_text, text=quote)                       #changes text to the quote

window = Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50, background="white")

canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
text_bubble_img = PhotoImage(file="/Users/jerry/Documents/python/api/kanye_quotes/text_bubble.png")
canvas.create_image(150, 207, image=text_bubble_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes Here", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="/Users/jerry/Documents/python/api/kanye_quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.config(bg="white", highlightbackground="white")
kanye_button.grid(row=1, column=0)




window.mainloop()
