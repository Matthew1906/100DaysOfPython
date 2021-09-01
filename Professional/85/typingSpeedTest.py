# Import modules
from tkinter import Tk, Label, PhotoImage, Canvas, Entry, Button
from dotenv import load_dotenv
from os import getenv
from time import time
from requests import get

# Load Environment variables
load_dotenv()

# CONSTANTS
API_KEY = getenv('API_KEY')
API_ENDPOINT = 'https://api.textgears.com/grammar'

# Global variables
start = True

# Functions
def get_errors(text:str):
    '''Look for number of errors from the text using textgears API'''
    spell_params = {
        'text': text,
        'key':API_KEY
    }
    spell_check = get(
        url=API_ENDPOINT, 
        params = spell_params
    ).json()['response']
    num_of_errors = len(spell_check['errors'])
    return num_of_errors

def calc_wpm():
    '''Calculate Word per minute'''
    global timer1, timer2
    time = (timer2-timer1)/60
    text = type_entry.get().strip()
    errors = get_errors(text)
    wpm = ((len(text)//5)-errors)//time
    speed_label.config(text=f'Word per minute (wpm): {wpm}')

def timer():
    '''start and stop timer'''
    global start, timer1, timer2
    if start:
        timer1 = time()
        start = False
        type_entry.delete(0, 'end')
        speed_label.config(text='')
        prompt.config(text='Stop')
    else:
        timer2 = time()
        start = True
        calc_wpm()
        prompt.config(text='Start')


# Configure Window
window = Tk()
window.title('Typing Speed Test')
window.config(padx=40, pady=30)

# Configure PhotoImage
logo_image = PhotoImage(file='./assets/typing.png')

# Configure Canvas
canvas = Canvas(width = 150, height=150)
canvas.create_image(75, 75, image=logo_image)

# Configure Entry
type_entry = Entry()

# Configure Label
speed_label = Label(text='', bg='white')

# Configure Button
prompt = Button(text='Start', padx=10, command=timer)

# Layout
canvas.grid(row=0, column=0, columnspan=2)
type_entry.grid(row=1, column=0, pady=10)
prompt.grid(row=1, column=1, pady=10, padx=10)
speed_label.grid(row=2, column=0, columnspan=2, sticky='EW')

# Driver code
window.mainloop()