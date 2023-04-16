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
    try:
        ditc_french_words.remove(current_card)
    except ValueError:
        pass
    else:
        print(len(ditc_french_words))
        pd.DataFrame.from_dict(ditc_french_words).to_csv("data/words_to_learn.csv", index=False)
        next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = rd.choice(ditc_french_words)
        print_card("French", img_front_card, BLACK)
    except IndexError:
        current_card ={
                "French": "Winner",
                "English": "Winner"
                }
        print_card("French",img_front_card,BLACK)
    finally:
        flip_timer = window.after(3000, flip_card)

def flip_card():
    print_card("English", img_back_card,WHITE)

def print_card(language, img_card, color):
    global current_card
    canvas.itemconfig(txt_lang, text=language, fill=color)
    canvas.itemconfig(txt_word, text=current_card[language], fill=color)
    canvas.itemconfig(canvas_image, image=img_card)

#Cards
try:
    df_french_words = pd.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    df_french_words =  pd.read_csv("data/french_words.csv")
finally:
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
