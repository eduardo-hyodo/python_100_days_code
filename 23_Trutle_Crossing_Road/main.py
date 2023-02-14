import time
import random as rd
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard
OTHER_STREET_SIDE = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.setup()

screen.onkey(player.go_up, "w")
screen.listen()

game_level = 0 
game_is_on = True
car_freq = 0
sleep_time = 0.1

while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    car_freq += 1

    car_manager.move_cars()
    if game_level == 10:
        game_is_on = False
        print("winner")
    elif player.ycor() > OTHER_STREET_SIDE:
        player.reset()
        time.sleep(1.1)
        car_freq = 0
        game_level += 1
        sleep_time -= 0.02
    elif car_freq % (10 - game_level) == 0 :
        car_manager.add_car(280, rd.randint(-260,260))
        car_freq = 0
    for car  in car_manager.cars:
        if car.distance(player.position()) <= 22:
            game_is_on = False
            print("Game over")
screen.exitonclick()
