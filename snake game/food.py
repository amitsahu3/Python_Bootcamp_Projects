from turtle import Turtle
import random


class Food(Turtle):                 # Food is inherited from turtle

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('green')
        self.speed('fastest')           # creation and moving of food should not be seen
        random_x = random.randint(-280, 240)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh_food()


    # to move the food once the snake collides with it
    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
