from turtle import Turtle, Screen

t = Turtle()
screen =  Screen()


def move_forwads():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_clockwise():
    t.seth(t.heading()-5)

def turn_unclockwise():
    t.seth(t.heading()+5)

screen.listen()
screen.onkey(key="w", fun=move_forwads)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_unclockwise)
screen.onkey(key="c", fun=t.clear)
screen.exitonclick()
