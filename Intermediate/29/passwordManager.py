# Import Modules
# - Widgets
from tkinter import Tk, Button, Canvas, PhotoImage, Label, Entry
# - Message Boxes
from tkinter.messagebox import askyesno, showerror, showinfo
# - Random
from random import randint
# - Clipboard
from pyperclip import copy
# -JSON
import json
from json.decoder import JSONDecodeError

# 2. Password Generator
# List all numbers, alphabets, symbols
letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
numbers = "0 1 2 3 4 5 6 7 8 9".split(" ")
symbols = "! # $ % & ( ) * +".split(" ")

# I took this from previous project
def generate_password():
    password_length = 18
    password = ["_"]*password_length
    used_index = [False]*password_length
    # Uses Infinite looping for validation
    for _ in range(6):
        letter = letters[randint(1,len(letters)-1)]
        while True:
            index = randint(0,password_length-1)
            if not used_index[index]:
                used_index[index] = True
                password[index] = letter
                break
        symbol = symbols[randint(1,len(symbols)-1)]
        while True:
            index = randint(0,password_length-1)
            if not used_index[index]:
                used_index[index] = True
                password[index] = symbol
                break
        number = numbers[randint(1,len(numbers)-1)]
        while True:
            index = randint(0,password_length-1)
            if not used_index[index]:
                used_index[index] = True
                password[index] = number
                break
    # Clear the Entry
    password_input.delete(0,'end')
    # Insert the Generated Password to the Entry
    password_input.insert(0,''.join(password))
    # Copy Password to Clipboard
    copy(password_input.get())

# 3. Password Saver
def save_data():
    # Check if the input is empty
    if not password_input.get().strip() =='' and not name_input.get().strip()=='' and not website_input.get().strip()=="":
        # Confirm Dialog Box
        confirm = askyesno(title='Confirm Save', message='Are you sure you want to save the data?')
        if not confirm:
            return
        # Get Entry Input
        website = website_input.get().strip()
        name = name_input.get().strip()
        password = password_input.get().strip()
        # Append to File
        new_data={
            website:{
                'email':name,
                'password':password
            }
        }
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                update = True
                for website_name in data.keys():
                    if website == website_name:
                        confirm = askyesno(title='Confirm Save', message='Data already exist! Do you want to rewrite it?')
                        if confirm:
                           data[website]['email'] = name
                           data[website]['password'] = password 
                        update = False
                if update:
                    data.update(new_data)
        except JSONDecodeError:
            data = new_data
        except FileNotFoundError:
            data = new_data
        with open('data.json', 'w') as save_file:
            json.dump(data, save_file, indent=4)
        # Clear Input
        website_input.delete(0,'end')
        name_input.delete(0,'end')
        password_input.delete(0,'end')
    else:
        # Error Message
        showerror(title='Incomplete input', message = 'Your Input is incomplete!')

# 4. Search Data
def search():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
        website = website_input.get().strip()
        result = data[website]
    except FileNotFoundError:
        showerror(title='File not found!', message = 'File not found!')
    except KeyError:
        showerror(title='Data not found!', message = "Data not found!")
    else:
        result = f"Email/Username: {result['email']}\nPassword:{result['password']}"
        showinfo(title = website, message = result)

# 5. UI Setup

# Screen
screen = Tk()
screen.title("Password Manager")
screen.config(padx=40, pady=40)

# Image
logo_image = PhotoImage(file = 'logo.png')

# Canvas
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100,100, image=logo_image)

# Label
website_label = Label(text ='Website:',padx=10)
name_label = Label(text='Email/Username:',padx=10)
password_label = Label(text ='Password:',padx=10)

# Entry
website_input = Entry(width=35)
website_input.focus()
name_input = Entry(width=35)
password_input = Entry(width=21)

# Button
search_button = Button(text='Search', command = search)
pass_generator = Button(text='Generate Password',command=generate_password)
save_password = Button(text='Add',width=36, command=save_data)

# Layout
canvas.grid(row = 0, column = 1)
website_label.grid(row=1, column=0, sticky='EW')
name_label.grid(row=2, column=0, sticky='EW')
password_label.grid(row=3,column=0, sticky='EW')
website_input.grid(row=1, column=1, sticky='EW')
name_input.grid(row=2, column=1, columnspan=2, sticky='EW')
password_input.grid(row=3, column=1, sticky='EW')
search_button.grid(row=1, column=2,sticky='EW')
pass_generator.grid(row=3,column=2, sticky='EW')
save_password.grid(row=4, column=1, columnspan=2, sticky='EW')

# Main Loop
screen.mainloop()