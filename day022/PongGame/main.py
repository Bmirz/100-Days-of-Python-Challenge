#-------IMPORTS-------
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#-------Global Variables-------
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Classic Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard((20, 225))
l_scoreboard = Scoreboard((-20, 225))

game_over = False

#Creates Event Listener for Snake's movement
screen.listen()
screen.onkey(r_paddle.go_up, ("Up"))
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, ("w"))
screen.onkey(l_paddle.go_down, "s")


while game_over == False:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect ball and top/bottom wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()

    #Detect when R or L paddle misses
    if ball.xcor() > 380:
        l_scoreboard.point_up()
        ball.reset_position()

    elif ball.xcor() < -380:
        r_scoreboard.point_up()
        ball.reset_position()


    

screen.exitonclick()