from turtle import Screen,Turtle
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Xperia')
screen.tracer(0)


starting_postions=[(0,0),(-20,0),(-40,0)]

segments=[]

for position in starting_postions:
    new_segment=Turtle('square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(position)
    new_segment.penup()
    new_segment.speed(10)
    segments.append(new_segment)

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(segments)-1,0,-1):
        x=segments[segment-1].xcor()
        y=segments[segment-1].ycor()
        segments[segment].goto(x,y)

    segments[0].forward(20)
    segments[0].left(90)
        
        
    






























screen.exitonclick()