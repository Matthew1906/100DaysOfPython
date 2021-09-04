# Import modules
from tkinter import Button, Label, Tk, Text
from database import db
from random import choice

# Config Functions
def disappear():
    global pre, to
    to = writer_input.get("1.0", "end")
    print(to)
    if (pre != None and pre!=to) or (pre == None and len(to)!= 0):
        # Previous != Current or No Previous, but Current isn't empty
        pre = to
        screen.after(5000, disappear)
    else:
        # Remove the contents of the entry
        start_button.config(state='normal')
        writer_input.delete("1.0", "end")

def start():
    global pre
    pre = None
    text = choice(db)
    writer_input.insert("1.0", text)
    writer_input.focus()
    start_button.config(state='disabled')
    screen.after(5000, disappear)

# Config Screen
screen = Tk()
screen.title("Disappearing Text Writing Application")
screen.config(padx=40, pady=20)

# Config Labels
instruction_label = Label(text="Don't stop typing! All progress will be lost!")

# Config Button
start_button = Button(text='Start', command=start)

# Config Text Area
writer_input = Text(height=20)

# Layout
instruction_label.grid(row=0, column=0, sticky='EW')
start_button.grid(row=0, column=1, sticky='EW')
writer_input.grid(row=1, column=0, columnspan=2, pady=30)

# Start App
screen.mainloop()