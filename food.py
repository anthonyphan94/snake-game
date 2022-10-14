from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed('fastest')
        self.move_food()




    def move_food(self):
        random_x = random.randint(int(-1140/2), int(1140/2))
        random_y = random.randint(int(-1140/2), int(1140/2))
        self.goto(random_x, random_y)
