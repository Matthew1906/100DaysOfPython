# Day 81 of 100 Days of Python
# Project Name: Text to Morse Code Converter
# Things i implemented: dictionary, json, audio, function, and recursion

# Import modules
from morseConverter import morse_converter, DOT, DASH
from art import logo
from os import system, name
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
from json import dump, load
from json.decoder import JSONDecodeError

# Constants
WORD_GAP = "/"

# Functions
def clear():
    '''Library Way to clear screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def dot_sound(count:int):
    '''Play sound'''
    audio = AudioSegment.from_mp3('dot.mp3')
    play(audio*count)

def text_to_morse(text:str):
    '''Convert Text to Morse Code (in text form)'''
    result = ''
    for letter in text:
        morse = morse_converter.get(letter)
        if morse==None and letter == ' ':
            result+= WORD_GAP
        else:
            result+=morse + " "
    return result

def morse_to_audio(morse_code:str):
    '''Convert the morse code into audio'''
    words = morse_code.split('/')
    for word in words:
        # Each word
        letters = word.split()
        for letter in letters:
            # Each letter
            for element in letter:
                # Each element    
                if element == DOT:
                    dot_sound(1)
                elif element == DASH:
                    dot_sound(3)
            sleep(1.5)
        sleep(3.5)
    return

def save_to_json(text:str, morse_code:str):
    '''Save conversion data into json'''
    new_data = {
        text:{
            # Switch back to dots and dashes instead of cool unicode:v
            'morse_code':morse_code.replace(DOT,'.').replace(DASH, '-')
        }
    }
    try:
        with open('conversion_data.json','r') as file:
            data = load(file)
            for name in data.keys():
                if name==text:
                    return
        data.update(new_data)
    except FileNotFoundError:
        data = new_data
    except JSONDecodeError:
        data = new_data
    with open('conversion_data.json','w') as file:
        dump(data, file, indent=4)  
    return 

def load_data():
    '''Load existing data'''
    try:
        with open('conversion_data.json','r') as file:
            data = load(file)
    except FileNotFoundError:
        return
    except JSONDecodeError:
        return
    index = 1
    for key, value in data.items():
        # print(key)
        print(f'  {index}. {key} = {value["morse_code"].replace(".", DOT).replace("-", DASH)}')
        index+=1
    return

def start_app():
    '''Main App'''
    clear()
    print(logo)
    print(" Welcome to Text to Morse Code Converter! ")
    menu = input(" Type '1' to convert text into morse code, '2' to see converted texts!\n -> ").strip().lower()
    if menu=='1':
        text = input(" Insert your text to convert into morse code (ended in enter):\n -> ").lower().strip()
        morse_code = text_to_morse(text)
        print(f' Morse Code: {morse_code}')
        if input(" Type 'play' to play sound! ").strip().lower() == 'play':
            morse_to_audio(morse_code)
        save_to_json(text=text, morse_code=morse_code)
    elif menu=='2':
        load_data()
    if input(" Type 'y' to continue: ").strip().lower() == 'y':    
        start_app()

# Driver code
start_app()
print(" Thankyou for using this application!")