import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("The Pong Game")
my_screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

my_screen.listen()
my_screen.onkeypress(fun=right_paddle.up, key="Up")
my_screen.onkeypress(fun=right_paddle.down, key="Down")

my_screen.onkeypress(fun=left_paddle.up, key="w")
my_screen.onkeypress(fun=left_paddle.down, key="s")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect ball collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collision with right paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 and ball.dx > 0:
        ball.bounce_x()

    # Detect ball collision with left paddle.
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 and ball.dx < 0:
        ball.bounce_x()

    # Detect if the right paddle misses.
    if ball.xcor() > 380:
        ball.reset()
        ball.bounce_x()
        scoreboard.left_score()

    # Detect if the left paddle misses.
    if ball.xcor() < -380:
        ball.reset()
        ball.bounce_x()
        scoreboard.right_score()

my_screen.exitonclick()
