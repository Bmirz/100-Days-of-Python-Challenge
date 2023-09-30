from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(225,260)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over.", align=ALIGNMENT, font=FONT)


    def point_up(self):
        self.score +=1
        self.clear()
        self.update_score()
