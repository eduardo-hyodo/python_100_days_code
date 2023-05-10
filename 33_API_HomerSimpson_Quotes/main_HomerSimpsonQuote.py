import requests
from tkinter import Tk, Canvas, Button 

def get_quote():
    response = requests.get(url="https://thesimpsonsquoteapi.glitch.me/quotes")
    response.raise_for_status()
    canvas.itemconfig(quote_text, text=response.json()[0]["quote"])


window =  Tk()
window.title("Homer says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
quote_text = canvas.create_text(150,  207, text="Homer Simpson Quote Goes Here",
                                width=250,
                                font=("Arial"))
canvas.grid(row=0, column=0)

quote_button = Button(highlightthickness=0, command=get_quote, text="Get Quote")
quote_button.grid(row=1, column=0)

window.mainloop()
