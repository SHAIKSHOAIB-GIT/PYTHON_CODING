from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    q_text = questions["text"]
    q_answer = questions["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_q() 