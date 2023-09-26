#####Turtle Intro######

import turtle as t
from turtle import Screen
import random

timmy_turtle = t.Turtle()
timmy_turtle.shape("turtle")
screen = Screen()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

########### Challenge 4 - Random Walk ########
directions = [0, 90, 180 , 270]
timmy_turtle.pensize(10)
timmy_turtle.speed("fastest")

for index in range (250):
    timmy_turtle.color(random_color())
    timmy_turtle.forward(30)
    timmy_turtle.setheading(random.choice(directions))

timmy_turtle.reset()

screen.exitonclick()
