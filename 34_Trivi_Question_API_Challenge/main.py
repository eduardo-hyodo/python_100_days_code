from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

list_question = []

for question in question_data:
    o_question = Question(question["text"], question["answer"])
    list_question.append(o_question)

quiz = QuizBrain(list_question)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_question():
    quiz.next_question()
