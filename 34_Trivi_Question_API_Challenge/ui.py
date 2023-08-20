from tkinter import Tk, Label, Button, Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375262"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=350, height=250, bg="white")
        self.canvas.grid(row=0, column=0)

        self.button_true = Button(highlightthickness=0, text="True")
        self.button_false = Button(highlightthickness=0, text="False")

        self.score_lbl = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial")
        )
        self.score_lbl.grid(row=0, column=1)

        self.question_text = self.canvas.create_text(
            150, 50, width=200, fill=THEME_COLOR, text="Question in here"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
