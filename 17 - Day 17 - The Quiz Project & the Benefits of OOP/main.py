# class User:
#     def __init__(self, ID, name):
#         self.ID = ID
#         self.name = name
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user1 = User("001", "tejas")
# # user1.id = "001"
# # user1.username = "tejas"
# # print(user1.ID)
# # print(user1.followers)
# user2 = User("002", "jack")
# # user2.id = "002"
# # user2.username = "jack"
# # print(user2.name)
#
# user1.follow(user2)
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(i["question"], i["correct_answer"]) for i in question_data]

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.user_score}/{len(question_bank)}")
