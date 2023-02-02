from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

game_is_on = True

left_paddle = Paddle((-250,0))
right_paddle = Paddle((250,0))
ball = Ball((0,0))

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.listen()

while game_is_on:
    screen.update()
    time.sleep(0.25)

    ball.move()

screen.exitonclick()
