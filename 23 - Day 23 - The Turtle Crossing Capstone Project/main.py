import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()
car_manager.create_car()
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.show_score()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        scoreboard.increase_level()
        car_manager.level_up()
        player.go_to_start()

screen.exitonclick()
