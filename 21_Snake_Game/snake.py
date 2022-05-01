from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []
        self.turn = None
        self.turn_point = None
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
       for i in range(0,3):
           turtle = Turtle("square")
           turtle.color("white")
           turtle.penup()
           turtle.goto(x= -i *20.0, y=0.0)
           self.segments.append(turtle)
    
    def turn_right(self, seg):
        seg.right(90)
        return seg

    def turn_left(self, seg):
        seg.left(90)
        return seg

    def move_right(self):
        self.turn_point = self.segments[0].position()
        self.turn = self.turn_right

    def move_left(self):
        self.turn_point = self.segments[0].position()
        self.turn = self.turn_left

    def move(self):
        turn_point = None
        for seg in self.segments:
            if seg.position() == self.turn_point:
                seg = self.turn(seg)
            seg.forward(10)


 
