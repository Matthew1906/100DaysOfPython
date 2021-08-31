# Quiz Brain Class

class QuizBrain:

    def __init__(self, q_list):
        '''Quiz Brain Constructor'''
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        '''Check if there are more questions'''
        return self.question_number < len(self.question_list)

    def next_question(self):
        '''Get Next Question'''
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text} (True/False): "

    def check_answer(self, user_answer):
        '''Check if the answer is correct'''
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False