from turtle import Turtle

class Ball(Turtle):

    def __init__(self,starting_position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(starting_position)
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_y = self.ycor() + self.move_y
        new_x = self.xcor() + self.move_x 
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
