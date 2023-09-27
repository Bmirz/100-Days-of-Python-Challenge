import turtle as turtle_module
import random
import colorgram

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.goto(-180,-180)

# Extract all 48 colors from the image
colors = colorgram.extract('HirstPainting.jpg', 48)
number_of_dots = len(colors) - 1

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, colors[dot_count].rgb)
    tim.forward(50)


    if dot_count % 6 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(300)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
