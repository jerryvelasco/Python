from turtle import Turtle
import random

DIAGNOL_DIRECTION = [135, 45, 90]

"""controls the ball attributes, including the speed, how it reacts when it touches the paddle, and each sides of the screen"""
class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(.8, .8)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.xmove = 10
        self.ymove = 10
        self.ball_speed = 0.05

    def move_ball(self):
        new_xcor = self.xcor() + self.xmove
        new_ycor = self.ycor() + self.ymove
        self.goto(new_xcor, new_ycor)

    def bounce_off_wall(self):
        self.ymove *= -1

    def bounce_off_paddle(self):
        self.xmove *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.setposition(0,0)
        self.bounce_off_paddle()
        self.ball_speed = 0.05
