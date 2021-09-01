# Import Modules
from turtle import Screen, Turtle
import pandas as pd

# Setup Screen
screen = Screen()
screen.title("U.S. States Game")
screen.setup(width = 800, height=600)
screen.bgpic("./Project/states_img.gif")

# Setup Turtle
writer = Turtle()
writer.hideturtle()
writer.penup()

# Setup Data
state_df = pd.read_csv("./Project/50_states.csv")
states = state_df['state'].to_list()

# Setup condition
running = True

# Game Start
while running:
    guess = screen.textinput("Guess the State", "Input State Name:").title()
    if guess == 'Exit':
        name = screen.textinput("Save Data", "Your Name:")
        to_learn_df = pd.DataFrame(data = states, columns=['State'])
        to_learn_df.to_csv("./Project/To_Learn/"+"_".join(name.split())+".csv")
        break
    if guess in states:
        # The coordinates are a bit off (from the course, im not diligent enough to change it one by one :v)
        x = int(state_df[state_df['state']==guess]['x'])
        y = int(state_df[state_df['state']==guess]['y'])
        writer.goto(x=x,y=y)
        writer.write(guess)
        states.remove(guess)
    if len(states)==0:
        running = False

screen.exitonclick()