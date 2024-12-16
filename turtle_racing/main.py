from turtle import Turtle, Screen
import random

did_race_start = False
screen = Screen()
screen.setup(width=500,height=400)
screen.title("Turtle Racing")
user_bet = screen.textinput(title="make your bet", prompt=f"which turtle will win the race? Enter a color: (red, blue, green, orange, yellow, or purple): ")
colors = ["red", "blue", "green", "orange", "yellow", "purple"]

#holds the new turtles created 
all_turtles = []
y_cord = -70

game_score = Turtle()
game_score.hideturtle()

#creates the turtles 
for i in range(0, 6):
    
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_cord)
    y_cord += 30
    all_turtles.append(new_turtle)

if user_bet:
    did_race_start = True

while did_race_start:

    #checks crossed the right side of the xcoordinate first
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            did_race_start = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                game_score.clear()
                print(f"you've won! the {winning_color} turtle is the winner")
                game_score.write(f"you've won! the {winning_color} turtle is the winner", align="center", font=("Courier", 15, "normal"))
                game_score.goto(0,0)

            else:
                game_score.clear()
                print(f"you've lost! the {winning_color} turtle is the winner")
                game_score.write(f"you've lost! the {winning_color} turtle is the winner", align="center", font=("Courier", 15, "normal"))
                game_score.goto(0,0)

        #controls speed of each turtle        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()






"""examples"""
# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_left():
#     tim.setheading(tim.heading() + 5)

# def turn_right():
#     tim.setheading(tim.heading() - 5)

# def clear():
#     tim.reset()




# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=turn_left, key="a")
# screen.onkey(fun=turn_right, key="d")
# screen.onkey(fun=clear, key="c")
# screen.listen()


