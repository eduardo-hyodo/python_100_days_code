from turtle import Turtle

class Ball(Turtle):
    def __init__(self,starting_position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(starting_position)

    def move(self):
        new_y = self.ycor() + 20
        new_x = self.xcor() + 20
        self.goto(new_x, new_y)
