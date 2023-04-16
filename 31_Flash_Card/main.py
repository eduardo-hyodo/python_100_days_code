from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#ffffff"
FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(410,265, image=card_image)
canvas.create_text(400,150, text="Title", font=FONT_LANG)
canvas.create_text(400,263, text="Word", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
btn_right = Button(image=right_image, highlightthickness=0)
btn_right.grid(column=1,row=1)

wrong_image = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=wrong_image, highlightthickness=0)
btn_wrong.grid(column=0,row=1)


window.mainloop()
