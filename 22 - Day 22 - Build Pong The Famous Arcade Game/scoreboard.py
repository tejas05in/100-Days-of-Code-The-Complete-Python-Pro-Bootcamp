from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.r_score += 1
        self.update_scoreboard()
