#####Turtle Intro######

import turtle as t
from turtle import Screen
import random

timmy_turtle = t.Turtle()
timmy_turtle.shape("turtle")
screen = Screen()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180 , 270]
timmy_turtle.pensize(10)
timmy_turtle.speed("fastest")

for index in range (250):
    timmy_turtle.color(random.choice(colours))
    timmy_turtle.forward(30)
    timmy_turtle.setheading(random.choice(directions))

screen.exitonclick()
