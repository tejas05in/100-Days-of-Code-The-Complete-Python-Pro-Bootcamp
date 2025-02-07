#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as f:
    letter = f.read()

#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()
    names = [name.strip() for name in names]

#Replace the [name] placeholder with the actual name.
for name in names:
    message = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.write(message)
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp