from turtle import Turtle

FONT = ("Courier", 24, "normal")

"""screen text attributes"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)
        

    def write_level(self):
        self.clear()
        self.goto(-220,240)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
