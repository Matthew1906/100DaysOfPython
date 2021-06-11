# DAY 31 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: Flash Card
# THINGS I IMPLEMENTED: Tkinter Module, Pandas, Random, File Processing, Error Handling

# Different from the course since i made it by myself
# Less usage of Pandas, but similar mechanism

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'

# Import Modules
from tkinter import Tk, Canvas, Button, PhotoImage
from random import randint
import pandas as pd

# Read Data
understood = []

def str_to_int(string):
    res = 0
    for i in range(len(row)):
        res+= int(row[i])*(10**(len(row)-1-i))
    return res

try:
    with open("Project/data/learned.txt") as learned_data:
        temp = learned_data.read().split("\n")
        for row in temp:
            row = str_to_int(row)
            understood.append(row)
except FileNotFoundError:
    pass

vocab_dictionary = pd.read_csv("Project/data/french_words.csv").to_dict()
vocab_length = len(vocab_dictionary['French'])

# Keep Track of Data
vocab_index = 0
french_vocabulary = vocab_dictionary['French'][vocab_index]
english_vocabulary = vocab_dictionary['English'][vocab_index]

def change_vocab():
    '''Change Vocabulary'''
    global vocab_index, vocab_length, understood, english_vocabulary, french_vocabulary
    if len(understood) == vocab_length:
        # Clear the learned.txt and the understood list
        understood.clear()
        with open('Project/data/learned.txt','w') as save_file:
            save_file.write("")
    vocab_index = randint(0, vocab_length-1)
    while vocab_index in understood:
        vocab_index = randint(0, vocab_length-1)
    french_vocabulary = vocab_dictionary['French'][vocab_index]
    english_vocabulary = vocab_dictionary['English'][vocab_index]
    
# Immediately change cards
change_vocab()

def save_progress():
    '''Save Learned Vocabulary Index'''
    global understood
    understood.append(vocab_index)
    with open('Project/data/learned.txt','a') as save_file:
        save_file.write(f"{vocab_index}\n")
    change_vocab()

def switchcard():
    '''Flash Card Mechanism'''
    if flash_card.itemcget(language_text, 'text')=='French':
        flash_card.itemconfig(canvas_image, image = back_image)
        flash_card.itemconfig(language_text, text='English', fill = 'white')
        flash_card.itemconfig(vocab_text, text=english_vocabulary, fill = 'white')
    else:
        flash_card.itemconfig(canvas_image, image = front_image)
        flash_card.itemconfig(language_text, text='French', fill = 'black')
        flash_card.itemconfig(vocab_text, text=french_vocabulary, fill = 'black')
    screen.after(3000, switchcard)

# UI 
# - Screen
screen = Tk()
screen.title("Flash Card")
screen.config(padx=20, pady = 10, bg=BACKGROUND_COLOR)

# - Photo Images
right_image = PhotoImage(file='Project/images/right.png')
wrong_image = PhotoImage(file='Project/images/wrong.png')
front_image = PhotoImage(file='Project/images/card_front.png')
back_image = PhotoImage(file='Project/images/card_back.png')

# - Canvas
flash_card = Canvas(width = 800, height = 526)
flash_card.config(bg=BACKGROUND_COLOR, highlightthickness = 0)
canvas_image = flash_card.create_image(400,263, image = front_image)
language_text = flash_card.create_text(400, 140, text = 'French', fill = 'black', font = (FONT_NAME, 25, "italic"))
vocab_text = flash_card.create_text(400, 263, text = french_vocabulary, fill = 'black', font = (FONT_NAME, 45, "bold"))
screen.after(3000, switchcard)

# - Buttons
right_button = Button(bg= BACKGROUND_COLOR, image= right_image, width = 100, height = 100, borderwidth=0, command = save_progress)
wrong_button = Button(bg= BACKGROUND_COLOR, image= wrong_image, width = 100, height = 100, borderwidth=0, command = change_vocab)

# - Layout
flash_card.grid(row = 0, column=0, columnspan = 2)
wrong_button.grid(row = 1, column = 0)
right_button.grid(row = 1, column = 1)

# Screen Mainloop
screen.mainloop()
