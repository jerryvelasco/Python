from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

#screen attributes
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping pong")
screen.tracer(0)

line = Turtle()
line.color("white")
line.hideturtle()
line.penup()
line.goto(x=0, y=-280)
line.pendown()
line.left(90)
line.pensize(4)

for dash in range(19):
    line.forward(15)
    line.penup()
    line.forward(15)
    line.pendown()

score = Score()
ball = Ball()
left_paddle = Paddle(-370)
right_paddle = Paddle(360)


screen.onkey(fun=left_paddle.up, key='w')
screen.onkey(fun=left_paddle.down, key='s')
screen.onkey(fun=right_paddle.up, key='Up')
screen.onkey(fun=right_paddle.down, key='Down')
screen.listen()

continue_game = True 

while continue_game:
    
    screen.update()
    ball.move_ball()
    time.sleep(ball.ball_speed)


    #checks if ball touches top or bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()
    
    #checks if the ball touches the paddle
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_off_paddle()
    
    #checks if the ball touches the right side of the screen
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_left_score()

        if score.left_score > 5:
            score.game_over()
            continue_game = False
            
    #checks if the ball touches the left side of the screen        
    elif ball.xcor() < -380:
        ball.reset_position()
        score.increase_right_score()

        if score.right_score > 5:
            score.game_over()
            continue_game = False

screen.exitonclick()

