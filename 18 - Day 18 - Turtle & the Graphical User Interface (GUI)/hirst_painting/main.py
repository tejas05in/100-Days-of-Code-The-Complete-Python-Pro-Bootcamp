# Extract colors from image
# import colorgram
#
# colors = [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colorgram.extract("image.jpg", 10)]
from turtle import Turtle, Screen
from random import choice

tim = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41),
              (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()


def horizontal_dots(star_y):
    tim.teleport(-200, star_y)
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)


def hirst_paint(start_y=-200):
    for _ in range(10):
        horizontal_dots(start_y)
        start_y += 50


hirst_paint()
screen.exitonclick()
