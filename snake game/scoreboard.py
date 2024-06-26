from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        with open('scores.txt') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score:{self.score}   High score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('scores.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()
    
    def increase_score(self):
        self.score +=1
        self.update_score()