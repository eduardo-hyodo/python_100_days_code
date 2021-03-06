from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
snake_head = snake.segments[0]

screen.listen()
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="d", fun=snake.move_right)

while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    if snake_head.xcor() >= 300:
        game_is_on = False
    elif snake_head.xcor() <= -300:
        game_is_on = False
    elif snake_head.ycor() >= 300:
        game_is_on = False
    elif snake_head.ycor() <= -300:
        game_is_on = False

screen.exitonclick()
