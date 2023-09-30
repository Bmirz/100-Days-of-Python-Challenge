#-------IMPORTS-------
from turtle import Screen
from snake import Snake
import time

#-------Global Variables-------
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("grey")
screen.title("Snake Game Classic")
screen.tracer(0)

snake =Snake()

game_over = False

#Creates Event Listener for Snake's movement
screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_left, "Left")

while game_over == False:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()

