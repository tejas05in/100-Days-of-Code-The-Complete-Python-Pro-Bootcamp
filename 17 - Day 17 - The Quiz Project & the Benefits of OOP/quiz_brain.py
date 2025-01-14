class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.correct_answer = None
        self.user_answer = None
        self.user_score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print("You got it right!")
        else:
            print("Sorry, that was wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.user_score}/{self.question_number}")
        print("\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.correct_answer = question.answer
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        return self.check_answer(self.user_answer, self.correct_answer)
