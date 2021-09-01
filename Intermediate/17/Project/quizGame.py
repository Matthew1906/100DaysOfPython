# Import modules
from quiz_brain import QuizBrain
from quiz_data import question_data
from quiz_model import Question
from os import system, name

def clear():
    '''Library Way to clear screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Create a list of Questions (from quiz_model) taken from the question_data (from quiz_data)
question_bank = [Question(q['text'], q['answer']) for q in question_data]

def start_quiz():
    '''Quiz Game'''
    quiz = QuizBrain(question_bank)# Create new Quiz Brain
    while quiz.still_has_questions(): #Check if there are more questions
        clear()
        quiz.next_question()
        input(" Press enter to continue.. ")
    print(f" You got {quiz.score} out of {quiz.question_number}!!")
    if input("Do you want to play again? Type 'y' to play again!: ")=='y':
        start_quiz()
start_quiz()