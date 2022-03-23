from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True
turn_point = None
snake = Snake()
head_snake = snake.segments[0]

screen.listen()
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="d", fun=snake.move_right)

while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    if head_snake.xcor() >= 300:
        game_is_on = False
    elif head_snake.xcor() <= -300:
        game_is_on = False
    elif head_snake.ycor() >= 300:
        game_is_on = False
    elif head_snake.ycor() <= -300:
        game_is_on = False

screen.exitonclick()
