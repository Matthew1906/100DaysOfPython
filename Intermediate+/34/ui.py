THEME_COLOR = "#375362"

from tkinter import Tk, Canvas, Button, PhotoImage, Label
from quiz_brain import QuizBrain

class QuizUI:
    def __init__(self, quiz_brain:QuizBrain):
        '''Quiz Interface Constructor'''
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg =THEME_COLOR)
        yes = PhotoImage(file='./images/true.png')
        no = PhotoImage(file='./images/false.png')
        self.scoreLabel = Label(text = f'Score: {self.quiz_brain.score}', bg = THEME_COLOR, fg = 'white', highlightthickness = 0, font=['Arial', 12, 'normal'])
        self.yes_button = Button(image = yes, width = 100, height = 100, borderwidth = 0, bg= THEME_COLOR, command = self.true)
        self.no_button = Button(image = no, width = 100, height = 100, borderwidth = 0, bg= THEME_COLOR, command =self.false)
        self.canvas = Canvas(width=300, height=250, bg = 'white', borderwidth=0)
        self.question_text = self.canvas.create_text(150,125, width = 280, text = '', font = ['Arial', 20, 'italic'])
        self.scoreLabel.grid(row = 0, column = 1)
        self.canvas.grid(row= 1, column = 0, columnspan = 2, pady = 25)
        self.yes_button.grid(row = 2, column = 0)
        self.no_button.grid(row = 2, column = 1)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        '''Get Next Question from Quiz Brain'''
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.question_text, text = f'{self.quiz_brain.next_question()}')
        else:
            self.canvas.itemconfig(self.question_text, text = f"You got {self.quiz_brain.score} out of 10!")
            self.yes_button.config(state = 'disabled')
            self.no_button.config(state = 'disabled')

    def update_score(self):
        '''Update Score'''
        self.scoreLabel.config(text =  f'Score: {self.quiz_brain.score}')
    
    def update_screen(self):
        '''Update the Window'''
        self.canvas.config(bg="white")
        self.next_question()
        self.update_score()

    def false(self):
        '''Event Listener when the user clicked False Button'''
        if self.quiz_brain.check_answer("false"):
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.update_screen)
        
    def true(self):
        '''Event Listener when the user clicked True Button'''
        if self.quiz_brain.check_answer("true"):
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.update_screen)