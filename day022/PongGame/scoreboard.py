from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 36, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def point_up(self):
        self.score +=1
        self.clear()
        self.update_score()
