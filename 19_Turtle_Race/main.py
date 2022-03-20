from turtle import Turtle, Screen
import random

colors = ["red","green","blue", "black", "purple"]
turtles = []
screen = Screen()
user_bet = screen.textinput(title="Make your bet", 
                            prompt="Which turtle will win the race? enter a color: ")

for i in range(0,5):
    turtle = Turtle() 
    turtle.penup()
    turtle.color(colors[i])
    turtle.setx(-1000)
    turtle.sety(i * 50)
    turtle.pendown()
    turtles.append(turtle)

def move_forward(turtle):
    turtle.forward(10)

def is_there_a_winner():
    for turtle in turtles:
        if turtle.xcor() == 600:
            winner_turtle = turtle.pencolor()
            print(f"The turtle {winner_turtle} is the winner")
            if user_bet == winner_turtle:
                print("You've won")
            else:
                print("You've lost!")
            return True

while not is_there_a_winner():
    turtle_to_move = turtles[random.randint(0,4)]  
    move_forward(turtle_to_move)

screen.exitonclick()
