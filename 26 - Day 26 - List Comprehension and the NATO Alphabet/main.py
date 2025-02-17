# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_numbers = [i**2 for i in numbers]
# print(squared_numbers)
# even_numbers = [num for num in numbers if num%2==0]
# print(even_numbers)
# with open ("file1.txt" , "r") as file:
#     data1 = file.readlines()
#
# with open ("file2.txt" , "r") as file:
#     data2 = file.readlines()
#
# common = [int(num) for num in data1 if num in data2]
# common.sort()
# print(common)
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# # random_score = {name:random.randint(1,100) for name in names}
# random_score = {'Alex': 13, 'Beth': 15, 'Caroline': 100, 'Dave': 61, 'Eleanor': 10, 'Freddie': 69}
# passed_students = {name:score for (name,score) in random_score.items() if score > 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather_c ={
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day:value*9/5+32 for (day,value) in weather_c.items()}
# print(weather_f)

# student_dict = {
#     "student" : ["Angela","James","Lily"],
#     "score" : [56,76,98]
# }
# # looping through dict
# for key,value in student_dict.items():
#     print(key, value)

# import pandas as pd
# student_df = pd.DataFrame(student_dict)
# print(student_df)

# loop through dataframe

# for key, value in student_df.items():
#     print(key, value)

# loop through rows
# for (index, row) in student_df.iterrows():
#     if row.student == "Angela":
#         print(row.score)

# NATO - ALPHABET PROJECT
import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (_, row) in df.iterrows()}
user = input("Enter a word: ").upper()
print([nato[letter] for letter in user])