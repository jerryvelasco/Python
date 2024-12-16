from turtle import Turtle

UP=90
WIDTH=1
HEIGHT=5
MOVEMENT=30

"""controls the attributes of the left and right paddles"""
class Paddle(Turtle):
    
    def __init__(self, xcoordinate):
        super().__init__()
        
        self.shape("square")
        self.shapesize(WIDTH, HEIGHT)
        self.setheading(UP)
        self.color('white')
        self.penup()
        self.setposition(x=xcoordinate, y=0)

    def up(self):
        self.forward(MOVEMENT)

    def down(self):
        self.backward(MOVEMENT)