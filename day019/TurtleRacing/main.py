from turtle import Turtle, Screen
import random

start_race = False
screen = Screen()
screen.setup(width=500,height=400)
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cordinate = -120
all_turtles = []

for color in turtle_colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    y_cordinate += 30
    new_turtle.goto(x=-230, y= y_cordinate)
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your Wager", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    start_race = True

while start_race == True:
    for turtle in all_turtles:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() > 230:
            winner = turtle.pencolor().capitalize()
            start_race = False
        
if user_bet == winner:
    print(f"You were right! {user_bet} won the race!")
else:
    print(f"{winner} won the race :( Better luck next time!")

screen.exitonclick()
