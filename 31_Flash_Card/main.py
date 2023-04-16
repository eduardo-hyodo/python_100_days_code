from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#ffffff"
BLACK = "#000000"
FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
current_card = {}

def unknown_word():
    next_card()

def known_word():
    next_card()

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = rd.choice(ditc_french_words)
    canvas.itemconfig(txt_lang, text="French", fill=BLACK) 
    canvas.itemconfig(txt_word, text=current_card["French"], fill=BLACK)
    canvas.itemconfig(canvas_image, image=img_front_card)

    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card

    canvas.itemconfig(txt_lang, text="English", fill=WHITE)
    canvas.itemconfig(txt_word, text=current_card["English"], fill=WHITE)
    canvas.itemconfig(canvas_image, image=img_back_card)

#Cards
df_french_words =  pd.read_csv("data/french_words.csv")
# ditc_french_words = { row.French:row.English for (index, row) in df_french_words.iterrows()}
ditc_french_words = df_french_words.to_dict(orient="records")

#GUI
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front_card = PhotoImage(file="images/card_front.png")
img_back_card =  PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(410,265, image=img_front_card)
txt_lang = canvas.create_text(400,150, text="", font=FONT_LANG)
txt_word = canvas.create_text(400,263, text="", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
btn_right = Button(image=right_image, command=known_word, highlightthickness=0)
btn_right.grid(column=1,row=1)

wrong_image = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=wrong_image, command=unknown_word, highlightthickness=0)
btn_wrong.grid(column=0,row=1)

flip_timer =  window.after(3000,flip_card)
next_card()

window.mainloop()
