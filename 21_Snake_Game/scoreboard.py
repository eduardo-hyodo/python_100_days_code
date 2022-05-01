from turtle import Turtle

ALIGNMENT = "center"
FONT=("Arial", 12, "normal")

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.show_score()
        self.ht()

    def add_to_score(self):
       self.score += 1
       self.show_score()

    def show_score(self):
        self.clear()
        score_string = f"The score: {self.score}"
        self.write(
                arg=score_string,
                move=False,
                align=ALIGNMENT,
                font=FONT
        )
