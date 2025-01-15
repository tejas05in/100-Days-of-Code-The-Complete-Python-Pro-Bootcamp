from turtle import Turtle, Screen
from random import choice


def random_color():
    color = (choice(range(256)), choice(range(256)), choice(range(256)))
    return color


Screen().colormode(255)
tim = Turtle()

# colors = ["red", "blue", "green", "yellow", "cyan", "magenta", "cyan", "indigo", "violet", "orange", "pink", "purple",
#           "brown"]

# turn_angle = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fast")
# for i in range(100):
#     tim.pencolor(random_color())
#     tim.forward(25)
#     tim.setheading(choice(turn_angle))

## Spirograph
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.pencolor(random_color())
        tim.circle(radius=100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
