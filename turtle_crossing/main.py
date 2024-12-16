import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, key="Up")
game_is_on = True

while game_is_on:

    time.sleep(0.1)     #cars are created every .1 seconds on every iteration
    screen.update()     #updates the screen after the cars are created 

    car_manager.create_car()
    car_manager.move()
    scoreboard.write_level()
    
    #checks if the turtle reached the top of screen
    if player.reached_top():
        car_manager.level_up()
        scoreboard.increase_level()

    #loops through each of the cars created 
    for car in car_manager.cars:

        #checks if the distance between the car and the turtle is less than 20 pixels 
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()