from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.show_score()

    def increase_level(self):
        self.level += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
