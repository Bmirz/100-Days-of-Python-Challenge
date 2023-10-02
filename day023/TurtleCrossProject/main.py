import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#-------Global Variables-------
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
level = Scoreboard()
car_manager = CarManager()

#Creates Event Listener for turtle's movement
screen.listen()
screen.onkey(player.go_up, ("Up"))
screen.onkey(player.go_up, ("w"))

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with turtle and cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()
    
    #Detect collision with turtle and top of screen
    if player.ycor() > 280:
        level.point_up()
        player.reset_pos()
        car_manager.level_up()


screen.exitonclick()