# What is GUI?
# Graphical User Interface -> important, because its predecessor is Command Line Interface
# Windows -> first GUI by Microsoft, led conflict with Apple (mac lisa), when both of them stole it from Xeroc
# Xerox Parc -> the first creator of GUI, OOP, LAN, Mouse
# No longer using CLI or Turtle
from tkinter import Tk, Label, Button, Entry

# initialize the window
window = Tk()
window.title("GUI Introduction")
window.minsize(width = 500, height=300)
window.config(padx = 100, pady=200)

# Label
label1 = Label(text="Button Unclicked", font=['Courier',13, 'bold'])
#place it in the screen, automatically centered
# when hovered, there are less arguments than what exists
# some parameter arent listed -> advanced python arguments (*args, *kwargs)

input1  = Entry()

# Button
def button_clicked():
    label1['text'] = input1.get()

button1 = Button(text="First Button", command = button_clicked)
button2 = Button(text="Another Button", command = button_clicked)
# we can add event listener

# Entry Component -> input

label1.grid(row=0, column = 0)
button1.grid(row = 1, column = 1)
button2.grid(row=0, column=2)
input1.grid(row = 2, column=3)


# pack = top to down, hard to specify a precise position
# place = with coordinate (x=, y=)
# grid = divided into rows and columns
# don't mix them up -> error

# keep the window on screen -> at the end of program
window.mainloop()




