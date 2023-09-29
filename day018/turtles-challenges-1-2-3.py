#####Turtle Intro######

import turtle as t
from turtle import Screen
import random

timmy_turtle = t.Turtle()
timmy_turtle.shape("turtle")
screen = Screen()
trutle_colors = ["aquamarine", "steel blue", "violet", "dark orchid", "coral"]

######## Challenge 1 - Draw a Square ############
timmy_turtle.color(random.choice(trutle_colors))
for index in range(4):
    timmy_turtle.forward(100)
    timmy_turtle.right(90)

timmy_turtle.reset()


######### Challenge 2 - Draw a Dashed Line ######
timmy_turtle.color(random.choice(trutle_colors))
for index in range(10):
    timmy_turtle.forward(5)
    timmy_turtle.penup()
    timmy_turtle.forward(5)
    timmy_turtle.pendown()

timmy_turtle.reset()

########### Challenge 3 - Draw Shapes ########
def draw_shape(num_sides):
    angle = 360 / num_sides
    for index in range(num_sides):
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)


for shape_sides in range(3,11):
    timmy_turtle.color(random.choice(trutle_colors))
    draw_shape(shape_sides)


timmy_turtle.reset()

screen.exitonclick()
