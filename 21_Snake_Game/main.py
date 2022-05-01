from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="d", fun=snake.move_right)

while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    if snake.head.distance(food) < 15:
        food.respawn()

    if snake.head.xcor() >= 300:
        game_is_on = False
    elif snake.head.xcor() <= -300:
        game_is_on = False
    elif snake.head.ycor() >= 300:
        game_is_on = False
    elif snake.head.ycor() <= -300:
        game_is_on = False

screen.exitonclick()
