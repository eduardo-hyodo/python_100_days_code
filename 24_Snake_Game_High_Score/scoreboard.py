from turtle import Turtle

ALIGNMENT = "center"
FONT=("Arial", 12, "normal")

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.show_score()
        self.ht()

    def add_to_score(self):
       self.score += 1
       self.show_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0 
        self.show_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     score_string = "Game Over"
    #     self.write(
    #             arg=score_string,
    #             move=False,
    #             align=ALIGNMENT,
    #             font=FONT
    #     )

    def show_score(self):
        self.clear()
        score_string = f"The score: {self.score}  |  The High Score: {self.high_score}"
        self.write(
                arg=score_string,
                move=False,
                align=ALIGNMENT,
                font=FONT
        )
