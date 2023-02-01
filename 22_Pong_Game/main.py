from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

game_is_on = True

starting_position_paddle1 = [(-200, 20), (-200, 40), (-200, 60)]
paddle = Paddle(starting_position_paddle1)
starting_position_paddle2 = [(200, 20), (200, 40), (200, 60)]
paddle2 = Paddle(starting_position_paddle2)

screen.onkey(paddle.up, "w")
screen.onkey(paddle.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")
screen.listen()
# screen.onkey(paddle.up, "Up")
# screen.onkey(paddle.down, "Down")

while game_is_on:
    screen.update()
    time.sleep(0.195)
    paddle.move() 
    paddle2.move()

    #Detect collision with wall
    if paddle.head.ycor() > 290:
        paddle.down()
    if paddle.head.ycor() < -290:
        paddle.up()
    if paddle2.head.ycor() > 290:
        paddle2.down()
    if paddle2.head.ycor() < -290:
        paddle2.up()

screen.exitonclick()
