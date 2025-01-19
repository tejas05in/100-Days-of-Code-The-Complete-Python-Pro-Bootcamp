from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(0, 250)
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
