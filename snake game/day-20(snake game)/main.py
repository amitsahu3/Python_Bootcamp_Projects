# the bug in it is that segments break when speed is high

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# creating and setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)        # to off the drag animation ,use tracer.update after off


# to create snake and move snake
saanp = Snake()

# creating the food
food = Food()

# scoreboard
scoreboard = ScoreBoard()

# using key inputs with listen to move snake in other directions
screen.listen()
screen.onkey(fun=saanp.up, key='Up')
screen.onkey(fun=saanp.down, key='Down')
screen.onkey(fun=saanp.left, key='Left')
screen.onkey(fun=saanp.right, key='Right')


game_on = True
while game_on:
    screen.update()     # after 0.3 secs update the screen
    time.sleep(0.1)
    if saanp.pace == 30:
        time.sleep(0.01)       # to add a delays
    saanp.move_snake()

    # detect collision with food
    if saanp.head.distance(food) < 15:
        food.refresh_food()
        saanp.extend_snake()
        scoreboard.increase_score()
        saanp.increase_pace()
    # detect collision with wall
    if saanp.head.xcor() > 280 or saanp.head.xcor() < -280 or saanp.head.ycor() > 280 or saanp.head.ycor() < -280:
        scoreboard.reset()
        saanp.reset_snake()

    # detecting collision with itself
    for segment in saanp.segments[1:]:        # sliced so as to exclude the head

        if segment == saanp.head:
            pass
        elif saanp.head.distance(segment) < 10:
            scoreboard.reset()
            saanp.reset_snake()



screen.exitonclick()

