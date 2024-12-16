from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

"""Creates the turtle attributes"""
class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    """controls the turtles movement"""
    def move_forward(self):
        self.forward(MOVE_DISTANCE)


    """controls what happens if the turtle reaches the top of screen"""
    def reached_top(self):

        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        
        else:
            return False
        
