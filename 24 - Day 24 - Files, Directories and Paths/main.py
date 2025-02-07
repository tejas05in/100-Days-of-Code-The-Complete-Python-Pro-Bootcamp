# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# with open("my_file.txt","a") as file:
#     file.write("\nNew text.")

# with open("C:/Users/tejas/Desktop/my_file.txt", "w") as file:
#     file.write("New text.")

with open("../../requirements.txt") as f:
    requirements = f.read().splitlines()
    print(requirements)