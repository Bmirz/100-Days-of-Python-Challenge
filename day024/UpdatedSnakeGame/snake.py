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
        '''Creates inital snake body (3 segments)'''
        for position in STARTING_POSITIONS:
            self.grow_snake(position)

    def reset(self):
        '''Gets rid of old snake body, clears 'snake_body list, and creates a new base snake'''
        for seg in self.snake_body:
            seg.goto(-700,700)
        self.snake_body.clear()
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def extend_snake(self):
        '''Creates another segment at the end of snakes body'''
        self.grow_snake(self.snake_body[-1].position())

    def move(self):
        '''Handles snake_body segments coordinated following of snake_head'''
        for seg_num in range(len(self.snake_body)-1, 0,-1):
            new_x = self.snake_body[seg_num -1].xcor()
            new_y = self.snake_body[seg_num -1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_SPEED)

    def turn_up(self):
        '''Ensures snake never backtracks while moving up, causing unintenional game over'''
        if(self.snake_head.heading()!= DOWN and self.snake_head.heading()!= UP):
            self.snake_head.setheading(UP)

    def turn_down(self):
        '''Ensures snake never backtracks while moving down, causing unintenional game over'''
        if(self.snake_head.heading()!= UP and self.snake_head.heading()!= DOWN):
            self.snake_head.setheading(DOWN)

    def turn_right(self):
        '''Ensures snake never backtracks while moving right, causing unintenional game over'''
        if(self.snake_head.heading()!= LEFT and self.snake_head.heading()!= RIGHT):
            self.snake_head.setheading(RIGHT)

    def turn_left(self):
        '''Ensures snake never backtracks while moving left, causing unintenional game over'''
        if(self.snake_head.heading()!= RIGHT and self.snake_head.heading()!= LEFT):
            self.snake_head.setheading(LEFT)