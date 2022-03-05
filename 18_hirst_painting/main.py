import colorgram
import turtle as t
import random as r

t.colormode(255)
#colors =  colorgram.extract("image.jpg",30)
#colors_tuples = []
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    colors_tuples.append(new_color)
colors_rgb = [(44, 95, 148), (180, 45, 75), (227, 207, 100), (209, 156, 90), (179, 169, 34), (136, 88, 62), (117, 178, 208), (200, 76, 122), (213, 130, 173), (228, 70, 50), (91, 104, 189), (47, 165, 120), (21, 156, 85), (123, 217, 208), (52, 56, 91), (119, 46, 36), (118, 43, 72), (38, 185, 196), (226, 171, 188), (125, 187, 158), (176, 186, 217), (232, 174, 166), (154, 208, 217), (212, 205, 41), (43, 76, 80), (48, 50, 75)]

def random_color():
    return r.choice(colors_rgb) 


turtle = t.Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()
dot_per_line = 20
space_per_dot = 50
number_of_dots = 400

for i in range (0, number_of_dots):

    x = (int( i % dot_per_line ) * space_per_dot) - 500
    y = (int(i / dot_per_line) *  space_per_dot) - 300 
     
    turtle.setx(x)
    turtle.sety(y)
    turtle.dot(20,random_color())

screen = t.Screen() 
screen.exitonclick()
