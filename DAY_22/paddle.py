from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super(Paddle, self).__init__()
        self.create_segment(position)

    def create_segment(self, position):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
