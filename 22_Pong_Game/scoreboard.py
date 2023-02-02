from turtle import Turtle

ALIGNMENT = "center"
FONT=("Arial", 12, "normal")

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.left_points = 0
        self.right_points = 0
        self.winner = False
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.show_score()
        self.ht()

    def add_to_score(self,side):
        if side == "left":
            self.left_points += 1
        else:
            self.right_points += 1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        score_string = "Game Over"
        self.write(
                arg=score_string,
                move=False,
                align=ALIGNMENT,
                font=FONT
        )

    def has_winner(self):
        if self.left_points == 3:
            self.winner = True
        elif self.right_points == 3:
            self.winner = True
        return self.winner

    def show_score(self):
        self.clear()
        score_string = f"Left Points= {self.left_points} vs Right Points= {self.right_points}"
        self.write(
                arg=score_string,
                move=False,
                align=ALIGNMENT,
                font=FONT
        )
