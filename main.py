from turtle import Screen
from snake import Snake
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Xperia')
screen.tracer(0)
Saji=Snake()




is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    Saji.move_snake()
    
        
        
    






























screen.exitonclick()