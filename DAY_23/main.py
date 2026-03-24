import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
my_screen.listen()
my_screen.onkeypress(fun=player.move_up, key="Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    my_screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect player's collision with car.
    for car in car_manager.cars:
        if player.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Detect when the player crosses successfully.
    if player.finish_line():
        player.goto_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

my_screen.exitonclick()
