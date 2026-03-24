from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        self.penup()
        self.move_speed = 0.1
        self.dx = 10
        self.dy = 10

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def reset(self):
        new_x = self.xcor() * 0
        new_y = self.ycor() * 0
        self.move_speed = 0.1
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.dy *= -1
