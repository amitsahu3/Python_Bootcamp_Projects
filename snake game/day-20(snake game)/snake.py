from turtle import Turtle

# creating constants
# PACE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


# creating a list to add and maintain snake
class Snake():
    def __init__(self):

        # creating the snake body
        self.segments = []
        self.create_snake()
        self.pace = 10
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # resetting and creating a new snake from the center again
    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        # iterating in the reverse order to put segments in successive positions
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # to get hold of second last x and y coordinates
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(self.pace)  # above will move all segments except the head(1st segment) so move it manually
    def increase_pace(self):
        self.pace += 10
    def up(self):
        if self.head.heading() != DOWN:         # to avoid up and down movements simultnaeously
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)