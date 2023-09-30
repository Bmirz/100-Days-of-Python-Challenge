from turtle import Turtle
BASE_SPEED = 10
MOVE_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.x_move = BASE_SPEED
        self.y_move = BASE_SPEED
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def speed_up(self):
        self.move_speed /= 1.1
    
    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = MOVE_SPEED
        self.bounce_x()