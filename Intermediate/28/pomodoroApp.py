# IMPORT MODULES
from tkinter import Tk, Canvas, PhotoImage, Button, Label
import time

# CONSTANTS
PINK = "#FF449F"
RED = "#BF1363"
GREEN = "#1eae98"
YELLOW = "#fff5b7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = '✓'
reps  = 0
timer = None 

# TIMER RESET
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    todo_label['text'] = 'Timer'
    todo_label.config(fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label['text'] = ''
    

# TIMER MECHANISM
def work(): 
    todo_label['text'] = 'Work'
    todo_label.config(fg=GREEN)
    countdown(WORK_MIN*60)

def short_break():
    todo_label['text'] = 'Short Break'
    todo_label.config(fg=PINK)
    countdown(SHORT_BREAK_MIN*60)

def long_break():
    todo_label['text'] = 'Long Break'
    todo_label.config(fg=RED)
    countdown(LONG_BREAK_MIN*60)

def start_timer():
    global reps
    reps+=1
    if reps==8:
        long_break()
    elif reps<8 and reps%2==0:
        short_break()
    elif reps<8 and reps%2!=0:
        work()
        num_check = (reps+1)//2
        checks = CHECKMARK*num_check
        check_label.config(text = checks)
    else:
        reset_timer()
        return


# COUNTDOWN MECHANISM
def countdown(length):
    minutes = length//60
    if minutes<10:
        minutes = "0"+str(minutes)
    seconds = length%60
    if seconds<10:
        seconds = "0"+str(seconds)
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if length>0:
        global timer
        timer = window.after(1000, countdown ,length - 1)
    else:
        start_timer()

# 6. UI SETUP

# Window 
window = Tk()
window.title("Pomodoro")
window.config(padx = 70, pady = 15, bg=YELLOW)

# PhotoImage
tomato = PhotoImage(file ="tomato.png")

# Canvas
canvas = Canvas(width = 200, height = 224)
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112,image = tomato)
timer_text = canvas.create_text(103,128, text = '00:00', fill = 'white', font = (FONT_NAME, 35, "bold"))

# Label
check_label = Label(text = '', bg = YELLOW, fg = GREEN, font = (FONT_NAME, 15, 'normal'))
check_label.config(pady=  25)

todo_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = [FONT_NAME, 35, 'bold'])
todo_label.config(pady = 25)

# Button
start_button = Button(text = "Start", command = start_timer)
reset_button = Button(text = 'Reset', command = reset_timer)

# Layout
todo_label.grid(row = 0, column = 1)
canvas.grid(row = 1, column = 1)
start_button.grid(row = 2, column = 0)
reset_button.grid(row = 2, column=2)
check_label.grid(row=3, column=1)

# mainloop
window.mainloop()