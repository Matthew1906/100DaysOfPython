from quiz_model import Question

# Basically Controller
class QuizBrain:
    def __init__(self, question_list):
        '''Initialize Starting Values'''
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def check_answer(self, player_answer, current_question):
        '''Check if the answer is correct'''
        if current_question.answer == player_answer:
            return True
        return False

    def next_question(self):
        '''Prompt the player to answer the question'''
        current_question = self.question_list[self.question_number]
        player_answer = input(f" Q.{self.question_number+1}: {current_question.text}. (True/False)?: ")
        self.question_number+=1
        if self.check_answer(player_answer, current_question):
            self.score+=1
            print(" You're correct")
        else:
            print(" You're wrong")
        print(f" Current Score: {self.score}/{self.question_number}.\n")
    
    def still_has_questions(self):
        '''Check if there are more questions'''
        if self.question_number < len(self.question_list):
            return True
        return False