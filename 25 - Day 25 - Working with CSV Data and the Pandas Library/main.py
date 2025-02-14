# with open("weather-data.csv") as file:
#     data = file.readlines()
#
# day = []
# temp = []
# condition = []
#
# for info in data[1:]:
#     text = info.strip().split(",")
#     day.append(text[0])
#     temp.append(text[1])
#     condition.append(text[2])
# print(day, temp, condition)

# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas as pd
# data = pd.read_csv("weather-data.csv")
# print(type(data))
# print(data.temp)
#
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# Average temperature
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in columns
# print(data["condition"])
# print(data.condition)

# Get data in the rows

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 9/5+ 32) # for farenhite conversion

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

df = pd.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# df['Primary Fur Color'].value_counts().to_frame().reset_index().reset_index().rename(columns={'index':"fur",'Primary Fur Color': 'colors'}).to_csv("squirrel_count.csv",index=False)

Gray = 0
Cinnamon = 0
Black = 0
for i in df['Primary Fur Color'].dropna():
    if i == 'Gray':
        Gray += 1
    elif i == 'Cinnamon':
        Cinnamon += 1
    elif i == 'Black':
        Black += 1
fur = [i for i in range(3)]
data = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "count": [Gray, Cinnamon, Black]
}
data_frame = pd.DataFrame(data)
data_frame.to_csv("squirrel_count.csv")