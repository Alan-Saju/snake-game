from turtle import Turtle,Screen

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
       for position in STARTING_POSITIONS:
            new_segment=Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(position)
            new_segment.penup()
            new_segment.speed(10)
            self.segments.append(new_segment)
    def move_snake(self):
        for segment in range(len(self.segments)-1,0,-1):
            x=self.segments[segment-1].xcor()
            y=self.segments[segment-1].ycor()
            self.segments[segment].goto(x,y)
        self.segments[0].forward(MOVE_DISTANCE)

