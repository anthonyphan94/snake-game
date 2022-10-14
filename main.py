# Create a Snake Body
# Move the Snake
# Control the Snake
# Detect collision with food
# Create scoreboard
# Detect Collision with walls
# Detect collision with tails
import turtle
from turtle import Screen
import time
from snake import Snake
from food import *
from scoreboard import *

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 20:
        snake.add_segment()
        snake.add_segment()
        snake.add_segment()
        food.move_food()
        scoreboard.add_score()

    if snake.head.xcor() > 600 or snake.head.xcor() < -600 or snake.head.ycor() > 490 or snake.head.ycor() < -580:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1::]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
