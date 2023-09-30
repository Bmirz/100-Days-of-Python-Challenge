from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def grow_snake(self, position):
        '''Creates snake's body in segmented objects'''
        new_segment = Turtle(shape="square")
        new_segment.color("greenyellow")
        new_segment.pencolor("black")
        new_segment.speed("fast")
        new_segment.penup()
        new_segment.shapesize(1,1,0.5)
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.grow_snake(position)

    def extend_snake(self):
        self.grow_snake(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0,-1):
            new_x = self.snake_body[seg_num -1].xcor()
            new_y = self.snake_body[seg_num -1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_SPEED)

    def turn_up(self):
        if(self.snake_head.heading()!= DOWN and self.snake_head.heading()!= UP):
            self.snake_head.setheading(UP)

    def turn_down(self):
        if(self.snake_head.heading()!= UP and self.snake_head.heading()!= DOWN):
            self.snake_head.setheading(DOWN)

    def turn_right(self):
        if(self.snake_head.heading()!= LEFT and self.snake_head.heading()!= RIGHT):
            self.snake_head.setheading(RIGHT)

    def turn_left(self):
        if(self.snake_head.heading()!= RIGHT and self.snake_head.heading()!= LEFT):
            self.snake_head.setheading(LEFT)
