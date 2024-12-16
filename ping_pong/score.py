from turtle import Turtle

"""holds the score attributes and controls how the score is updated"""
class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.write_scores()

    def write_scores(self):
        self.clear()
        self.goto(x=-100, y=220)
        self.write(f"{self.left_score}", align="center", font=("Courier", 75, 'normal'))
        self.goto(x=100, y=220)
        self.write(f"{self.right_score}", align="center", font=("Courier", 75, 'normal'))

    def increase_left_score(self):
        self.left_score += 1
        self.write_scores()

    def increase_right_score(self):
        self.right_score += 1
        self.write_scores()

    def game_over(self):
        self.goto(0,0)
        if self.right_score > 5:
            winner = "RIGHT SIDE"
        elif self.left_score > 5:
            winner = 'LEFT SIDE'
            
        self.write(f"GAME OVER, {winner} WINS!", align="center", font=("Courier", 35, 'normal'))


        