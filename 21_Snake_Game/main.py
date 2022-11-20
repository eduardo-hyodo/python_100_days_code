from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
score_board = Scoreboard() 

screen.listen()
#screen.onkey(key="a", fun=snake.move_left)
#screen.onkey(key="d", fun=snake.move_right)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.085)

    snake.move()

    #Detect collision with food 
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend()
        score_board.add_to_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.game_over()
        game_is_on = False

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 5:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
