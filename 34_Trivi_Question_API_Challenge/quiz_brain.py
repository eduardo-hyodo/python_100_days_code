import html

class QuizBrain:

    def __init__(self, o_question_list):
        self.question_number = 0
        self.question_list = o_question_list 
        self.score = 0

    def still_has_question(self):
        if self.question_number ==  len(self.question_list):
            return False
        return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question.text)
        return f"Q.{self.question_number}: {q_text}. (True/False)?: "

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"your current score is: {self.score}/{len(self.question_list)}")
