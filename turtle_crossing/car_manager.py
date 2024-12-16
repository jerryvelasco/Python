from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

"""creates the car attributes"""
class CarManager:

    def __init__(self):
        #holds all the cars created 
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    """creates car"""
    def create_car(self):

        #controls frequency of when cars are being created
        #theres a 1 and 6 chance that a car will be created every iteration 
        random_choice = random.randint(0,6)

        #cars will only be created when the num generated is 1 
        if random_choice == 1:

            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-260, 260)
            new_car.goto(300, random_y)
            self.cars.append(new_car)
    

    """controls car movement"""
    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)


    """will increase car speed if turtle reaches the top of screen"""
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
