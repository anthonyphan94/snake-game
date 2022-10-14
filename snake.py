from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANT = 30

print(STARTING_POSITION[-1][0])

UP = 90
DOWN = 270
RIGHT= 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in range(len(STARTING_POSITION)):
            segment = Turtle()
            segment.penup()
            segment.shape('square')
            segment.color('white')
            segment.penup()
            segment.goto(STARTING_POSITION[position])
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self):

        segment = Turtle()


        segment.shape('square')
        segment.speed('fastest')
        segment.color('black')

        segment.penup()
        new_position = (STARTING_POSITION[-1][0] - 20, 0)


        segment.goto(new_position)
        segment.color('white')


        # segment.speed('fastest')


        self.segments.append(segment)
