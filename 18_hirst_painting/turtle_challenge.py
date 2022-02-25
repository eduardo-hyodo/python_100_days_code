from turtle import Turtle, Screen

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

for i in range(0,50):
    timmy_the_turtle.forward(5)
    if i % 2 == 0:
        timmy_the_turtle.penup()
    else:
        timmy_the_turtle.pendown()




screen = Screen()
screen.exitonclick()
