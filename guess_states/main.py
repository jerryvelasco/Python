import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

user_guess = screen.textinput(title="Guess the state", prompt="What's another state name?: ").title()
csv_data = pandas.read_csv("50_states.csv")
states_only = csv_data.state.to_list()

continue_game = True
correct_guess = 0 
guessed_states = []

while continue_game:
    
    if correct_guess > 50 or user_guess == None or user_guess == "Exit":

        missed_states = [state for state in states_only if state not in guessed_states]
        new_df = pandas.DataFrame(missed_states)
        new_df.to_csv("missing_states.csv")
        continue_game = False
    
    if user_guess in states_only:

        state_info = csv_data[csv_data.state == user_guess]
        xcord = int(state_info.x)
        ycord = int(state_info.y)

        write_text = turtle.Turtle()
        write_text.penup()
        write_text.hideturtle()
        write_text.goto(xcord, ycord)
        write_text.write(user_guess)

        guessed_states.append(user_guess)
        correct_guess += 1

    user_guess = screen.textinput(title=f"{correct_guess}/50 Correct States", prompt="What's another state name?: ").title()



screen.exitonclick()

"""will get the coordinates of clicks we make on screen""" 
# #takes 2 values as input and prints them out
# def get_mouse_click_coordinates(x,y):
#  ı   print(x,y)

# #event listener, listens for when the mouse clicks and then its going to call method
# turtle.onscreenclick(get_mouse_click_coordinates)

#keeps the screen open 
# turtle.mainloop()


