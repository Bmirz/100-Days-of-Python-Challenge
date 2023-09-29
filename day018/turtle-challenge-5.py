#####Turtle Intro######

import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
screen = Screen()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
for index in range(36):
    tim.color(random_color())
    tim.speed("fastest")
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

screen.exitonclick()
