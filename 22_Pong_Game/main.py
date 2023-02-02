from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

game_is_on = True

paddle = Paddle((-250,0))
paddle2 = Paddle((250,0))

screen.onkey(paddle.go_up, "w")
screen.onkey(paddle.go_down, "s")
screen.onkey(paddle2.go_up, "Up")
screen.onkey(paddle2.go_down, "Down")
screen.listen()

while game_is_on:
    screen.update()
    time.sleep(0.195)

screen.exitonclick()
