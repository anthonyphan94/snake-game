from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 500)
        self.penup()
        self.score = 0
        self.color('white')
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def add_score(self):
        self.score += 20
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over Bitch", align="center", font=("Arial", 20, "normal"))
