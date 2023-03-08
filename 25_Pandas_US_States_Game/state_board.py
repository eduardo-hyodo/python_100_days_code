from turtle import Turtle

ALIGNMENT = "center"
FONT=("Arial", 9, "normal")

class StateBoard (Turtle):

    def __init__(self, name, cor_x, cor_y):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(cor_x,cor_y)
        self.ht()
        score_string = f"{name}"
        self.write(
                arg=score_string,
                move=False,
                align=ALIGNMENT,
                font=FONT
        )
