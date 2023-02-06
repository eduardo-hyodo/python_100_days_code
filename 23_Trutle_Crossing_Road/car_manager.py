from turtle import Turtle
import random as rd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_PER_LEVEL = 20


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def setup(self):
        for i in range(1,CARS_PER_LEVEL):
            self.add_car(rd.randint(-280,280),rd.randint(-260,260))

    def add_car(self,x,y):
        car = Turtle()
        car.shape("square")
        car.color(rd.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(x,y)
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
