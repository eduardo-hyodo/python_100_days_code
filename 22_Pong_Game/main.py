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

    #Detect collision with the top wall
    if ball.distance(y=300,x=ball.xcor()) < 15:
        ball.bounce_y()
    
    #Detect collision with the bottom wall
    if ball.distance(y=-300,x=ball.xcor()) < 15:
        ball.bounce_y()

    #Detect if ball it outreach 
    if ball.xcor() > 290:
        #player 1 gets a point
        print("player 1 gets a point")
        game_is_on = False

    if ball.xcor() < -290:
        #player 2 gets a point
        print("player 2 gets a point")
        game_is_on = False
   
    #Detect collision with the paddles
    if ball.distance(right_paddle) < 80 and ball.xcor() > 230:
        print("collision with the paddle")
        ball.bounce_x()

    if ball.distance(left_paddle) < 80 and ball.xcor() < -230:
        print("collision with the paddle")
        ball.bounce_x()


screen.exitonclick()
