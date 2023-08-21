from tkinter import Tk, Label, Button, Canvas
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375262"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=350, height=250, bg="white")
        self.canvas.grid(row=0, column=0)

        self.button_true = Button(highlightthickness=0, text="True",
                                  command=self.check_true)
        self.button_false = Button(highlightthickness=0, text="False", command=self.check_false)

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
        self.canvas.config(bg="white")
        self.check_score()
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="There are no more question")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def check_false(self):
        answer = self.quiz.check_answer(user_answer="false")
        self.feedback_answer(answer)

    def check_true(self):
        answer = self.quiz.check_answer(user_answer="true")
        self.feedback_answer(answer)
    
    def check_score(self):
        score = f"Score: {self.quiz.score}"
        self.score_lbl.config(text=score)

    def feedback_answer(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question) 
