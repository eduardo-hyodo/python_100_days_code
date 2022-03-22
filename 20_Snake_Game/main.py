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

def move_right(seg):
    seg.goto(seg.xcor() + 10, seg.ycor())
    return seg

def move_up(seg):
    seg.goto(seg.xcor(), seg.ycor() + 10)
    return seg

def move_left(seg):
    seg.goto(seg.xcor() - 10, seg.ycor())
    return seg

def move_down(seg):
    seg.goto(seg.xcor(), seg.ycor() - 10)
    return seg

game_is_on = True
head_snake = snake[0]
current_movement = move_right
new_movement = None

while game_is_on:
    screen.update()
    time.sleep(0.05)

    #Move Snake
    if head_snake.xcor() == 150:
        new_movement = move_left

    if head_snake.xcor() == -150:
        new_movement = move_up

    #TODO add turn to whole body
    for seg in snake:
        if new_movement != None:
            seg = new_movement(seg)
            #current_movement = new_movement
            #new_movement = None
        else:
            seg =  current_movement(seg)

    if head_snake.xcor() >= 300:
        game_is_on = False
    elif head_snake.xcor() <= -300:
        game_is_on = False
    elif head_snake.ycor() >= 300:
        game_is_on = False
    elif head_snake.ycor() <= -300:
        game_is_on = False

screen.exitonclick()
