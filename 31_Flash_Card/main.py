from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#ffffff"
FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
pair_words = {}

def unknown_word():
    next_card()

def known_word():
    next_card()

def next_card():
    global pair_words
    pair_words = rd.choice(ditc_french_words)

    canvas.itemconfig(txt_lang, text="French") 
    canvas.itemconfig(txt_word, text=pair_words["French"])


#Cards
df_french_words =  pd.read_csv("data/french_words.csv")
# ditc_french_words = { row.French:row.English for (index, row) in df_french_words.iterrows()}
ditc_french_words = df_french_words.to_dict(orient="records")

#GUI
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(410,265, image=card_image)
txt_lang = canvas.create_text(400,150, text="", font=FONT_LANG)
txt_word = canvas.create_text(400,263, text="", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
btn_right = Button(image=right_image, command=known_word, highlightthickness=0)
btn_right.grid(column=1,row=1)

wrong_image = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=wrong_image, command=unknown_word, highlightthickness=0)
btn_wrong.grid(column=0,row=1)
next_card()

window.mainloop()
