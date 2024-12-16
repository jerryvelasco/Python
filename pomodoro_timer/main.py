from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25               #duration of a work cycle 
SHORT_BREAK_MIN = 5         #happens after 1 work cycle
LONG_BREAK_MIN = 20         #happens after 
WORK_CYCLES = 0             #tracks works cycles 
CHECKMARKS = ""             
MY_TIMER = None



"""resets timer back to starting settings"""
def reset_timer():
    global WORK_CYCLES, CHECKMARKS

    #stops the timer 
    window.after_cancel(MY_TIMER)

    checkmark_label.config(text="")
    CHECKMARKS = ""
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    WORK_CYCLES = 0



"""starts the timer countdown"""
def start_timer():
    global WORK_CYCLES

    WORK_CYCLES += 1

    #converts minutes into secs
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    #calls countdown and changes screen the timer text if the cycles are at a certain work cycle
    if WORK_CYCLES % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=RED)

    elif WORK_CYCLES % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    
    else:
        count_down(work_secs)
        timer_label.config(text="Work")

        

"""controls the countdown subtracting 1 from timer"""
def count_down(timer_countdown):   
    global CHECKMARKS, MY_TIMER

    minute_countdown = math.floor(timer_countdown / 60)   #formats secs back to minutes without rounding up
    seconds_countdown = timer_countdown % 60              #finds the remainder 

    #formats seconds if its below 10 
    if seconds_countdown < 10:
        seconds_countdown = f"0{seconds_countdown}"    

    #updates time to 00:00 format
    canvas.itemconfig(timer_text, text=f"{minute_countdown}:{seconds_countdown}")

    if timer_countdown > 0:
        #waits 1 second, calls itself to keep looping, and subtracts 1 from timer number
        MY_TIMER = window.after(1000, count_down, timer_countdown - 1)

    else:
        #if the timer countdown is below 0 start_timer will start a another work cycle
        start_timer()

        #adds checkmarks to screen after every 2 work cycles
        if WORK_CYCLES % 2 == 0:
            CHECKMARKS += "✓"
            checkmark_label.config(text=CHECKMARKS)



"""UI setup"""
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)


#imports and places image on screen
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
checkmark_label.grid(column=1, row=3)


#buttons 
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
