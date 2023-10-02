#-------IMPORTS-------
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#-------Global Variables-------
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("grey")
screen.title("Snake Game Classic")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_over = False

#Creates Event Listener for Snake's movement
screen.listen()
screen.onkey(snake.turn_up, ("Up"))
screen.onkey(snake.turn_up, ("w"))
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_down, "s")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_right, "d")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_left, "a")

while game_over == False:
    screen.update()
    time.sleep(0.09)
    snake.move()

    #detect snake/food collision
    if snake.snake_head.distance(food) < 20:
        food.refresh()
        snake.extend_snake()
        score.point_up()

    #detect snake/wall collision
    if snake.snake_head.xcor() < - 300 or snake.snake_head.xcor() > 290 or snake.snake_head.ycor() < -300 or snake.snake_head.ycor() > 300:
        score.reset()
        snake.reset()

    #detect snake head/body collision
    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()