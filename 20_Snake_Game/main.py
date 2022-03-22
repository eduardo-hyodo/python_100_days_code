from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = []
for i in range(0,3):
    turtle = Turtle("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(x= -i *20.0, y=0.0)
    snake.append(turtle)

def turn_right(seg):
    seg.right(90)
    return seg

def turn_left(seg):
    seg.left(90)
    return seg

def move_right():
    turn_point == snake[0].position()
    turn = turn_right

def move_left():
    turn_point == snake[0].position()
    turn = turn_left


game_is_on = True
turn_point = None
head_snake = snake[0]

while game_is_on:
    screen.update()
    time.sleep(0.05)

    for seg in snake:
        if seg.position() == turn_point:
            seg = turn(seg)
        seg.forward(10)

    if head_snake.xcor() >= 300:
        game_is_on = False
    elif head_snake.xcor() <= -300:
        game_is_on = False
    elif head_snake.ycor() >= 300:
        game_is_on = False
    elif head_snake.ycor() <= -300:
        game_is_on = False

screen.onkey(key="a", fun=move_left)
screen.exitonclick()
