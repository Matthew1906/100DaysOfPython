# Turtle Objects
from turtle import Screen, Turtle
# Game Objects
from defender import Defender
from invaders import Invaders
from scoreboard import ScoreBoard
# Utilities
from time import sleep
from PIL import Image, ImageTk

# Initialize Screen
main_screen = Screen()
main_screen.title("Space Invaders")
main_screen.setup(width=800, height=550, startx= 250, starty=10)

# Setup Background
background_canvas = main_screen.getcanvas()

## Resize Image
image = Image.open("./images/space-bg.gif")
background_image = image.resize((800,550), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(background_image)

## Put image into background
background_canvas.create_image(0,0, image=background_image)

# Register shapes -> you need to resize the image first using PIL
main_screen.register_shape('./images/defender.gif')
main_screen.register_shape('./images/invader.gif')

# Add event listener
main_screen.tracer(0)
main_screen.listen()

# Menu indicator
is_game = False

# Menu drawing
menu = Turtle()
menu.hideturtle()
menu.penup()
menu.color('white')

def draw_menu():
    menu.goto((0,45))
    menu.write(f"Space Invaders", align = "center", font = ("Arial",24,"bold"))
    menu.goto((0,0))
    menu.write(f"Press 's' to start game", align = "center", font = ("Arial",12,"bold"))
    menu.goto((0,-35))
    menu.write(f"Press 'q' to quit game", align = "center", font = ("Arial",12,"bold")) 

def space_invaders():
    # Make sure that the game doesn't run multiple times
    menu.clear()
    global is_game
    if is_game:
        return
    is_game=True

    # Config game indicators
    running = True
    delay = 0.05

    # Objects   
    scoreboard = ScoreBoard()
    invaders = Invaders()
    defender = Defender()

    # Helper functions
    def clear_all():
        '''Reset all objects (except scoreboard)'''
        defender.reset_bullets()
        defender.reset()
        defender.hideturtle()
        invaders.reset()
        scoreboard.clear()

    def back_to_menu():
        '''Reset scoreboard and go back to menu'''
        scoreboard.reset()
        draw_menu()

    # Config listener
    main_screen.onkeypress(key='Left', fun=defender.left)
    main_screen.onkeypress(key='Right', fun=defender.right)
    main_screen.onkeypress(key='space', fun=defender.shoot)

    # start game
    while running:
        # Constant update of the main screen
        main_screen.update() 
        # Slight delay to prevent glitch
        sleep(delay)
        # Object's movements
        defender.move_bullets()
        invaders.move_invaders()
        invaders.move_bullets()
        # Check for collision
        if invaders.check_collision(defender):
            scoreboard.update_lives()
            defender.lose_life()
        elif defender.successful_shot(invaders.invaders):
            scoreboard.update_score()
        # Win condition
        if scoreboard.score == 560 or scoreboard.lives == 0:
            break
    clear_all()
    scoreboard.final_result()
    main_screen.ontimer(fun=back_to_menu, t=3000)
    is_game=False

draw_menu()
main_screen.onkey(key='s', fun=space_invaders)
main_screen.onkey(key='q', fun=main_screen.bye)
main_screen.mainloop()