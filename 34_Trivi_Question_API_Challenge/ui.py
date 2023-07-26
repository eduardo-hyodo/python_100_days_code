THEME_COLOR = "#375262"
from tkinter import Tk, Canvas, Button, Label

window = Tk()
window.title("Quizzler")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=400)
canvas.grid(row=0, column=0)

button_true = Button(highlightthickness=0, text="True")
button_false = Button(highlightthickness=0, text="False")

score_lbl = Label(text="Score:", font=("Arial"))
score_lbl.grid(row=0, column=1)

score_text = canvas.create_text( 300, 250, text="0", font=("Arial"))

question_text =  canvas.create_text( 150,
                                     270,
                                     text="Question in here",
                                     width=250,
                                     font=("Arial"))

button_true.grid(row=1, column=0)
button_false.grid(row=1, column=1)



window.mainloop()
