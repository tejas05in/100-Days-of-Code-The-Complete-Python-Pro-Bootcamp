import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()

def draw(x_cor,y_cor,answer):
    writer.teleport(x_cor,y_cor)
    writer.write(answer.title(),
                 align="center",
                 font=("Arial", 10, "bold"))
df = pd.read_csv("50_states.csv")
all_states = df.state.tolist()
guessed_states = []

game_on = True
while game_on and len(guessed_states) <50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What is another state name? or Type Exit to quit!").title()
    if answer_state == "Exit":
        game_on = False

    elif answer_state in all_states:
        guessed_states.append(answer_state)
        key = df[df["state"] == answer_state]
        x = int(key.x.item())
        y = int(key.y.item())
        draw(x, y, answer_state)
    else:
        print("Sorry, state not found. try again.")
else:
    draw(0,0,"Congratulations, you won!")

# States to learn.csv
to_learn = pd.Series(list(set(all_states)-set(guessed_states)))
to_learn.to_csv("States_to_learn.csv")