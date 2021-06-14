# DAY 34 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: Trivia Quiz App
# THINGS I IMPLEMENTED: Object Oriented Programming, Tkinter, API, REQUESTS, JSONS, HTML Module

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI
import html

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quizUI = QuizUI(quiz)