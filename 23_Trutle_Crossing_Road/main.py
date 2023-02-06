import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.setup()

screen.onkey(player.go_up, "w")
screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.move_cars()

screen.exitonclick()