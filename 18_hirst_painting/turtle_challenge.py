from turtle import Turtle, Screen
import random as r

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("blue")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)

#for i in range(0,50):
#    timmy_the_turtle.forward(5)
#    if i % 2 == 0:
#        timmy_the_turtle.penup()
#    else:
#        timmy_the_turtle.pendown()

# figures
#for i in range(3 , 9):
#    grd = 360.0 / i
#    for x in range(0,i):
#        timmy_the_turtle.forward(25)
#        timmy_the_turtle.right(grd)

colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
direction = [0, 90, 180, 270]
for i in range (1,1000):
    speed = i /10.0
    timmy_the_turtle.speed(i)
    timmy_the_turtle.color(r.choice(colors))
    timmy_the_turtle.pensize(speed)
    timmy_the_turtle.right(r.choice(direction))
    timmy_the_turtle.forward(30)

screen = Screen()
screen.exitonclick()
