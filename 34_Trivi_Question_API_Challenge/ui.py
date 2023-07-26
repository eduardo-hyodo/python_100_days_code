THEME_COLOR = "#375262"
from tkinter import Tk, Canvas, Button, Label

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50)

        self.canvas = Canvas(width=300, height=400)
        self.canvas.grid(row=0, column=0)

        self.button_true = Button(highlightthickness=0, text="True")
        self.button_false = Button(highlightthickness=0, text="False")

        self.score_lbl = Label(text="Score:", font=("Arial"))
        self.score_lbl.grid(row=0, column=1)

        self.score_text = self.canvas.create_text( 300, 250, text="0", font=("Arial"))

        self.question_text = self.canvas.create_text( 150,
                                             270,
                                             text="Question in here",
                                             width=250,
                                             font=("Arial"))

        self.button_true.grid(row=1, column=0)
        self.button_false.grid(row=1, column=1)
        self.window.mainloop()
