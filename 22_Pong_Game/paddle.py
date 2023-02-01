from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:
    def __init__(self, staring_positions):
        self.segments = []
        self.create_paddle(staring_positions)
        self.head = self.segments[0]
        self.head.setheading(UP)
    
    def create_paddle(self,staring_positions):
       for position in staring_positions:
           self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)


