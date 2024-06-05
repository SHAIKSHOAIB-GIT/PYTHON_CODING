
class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)
       
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     False

    def next_q(self):
        c_question = self.question_list[self.question_number]
        self.question_number +=1
        answer = input(f"Q.{self.question_number}: {c_question.text} (True/False)?: ")
        self.check_answer(answer, c_question.answer)

    def check_answer(self, answer, c_answer):
        if answer.lower() == c_answer.lower():
            self.score +=1
            print(f"you got it")
            print(f"your score is {self.score} ")
        else:
            print(f"you are wrong")
        print(f"your score is :{self.score}/{self.question_number}")