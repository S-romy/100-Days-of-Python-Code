import random
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(x=0, y=160)
writer.write("Turtle Racing Game", align="center", font=("Arial", 16, "bold"))

index = 0
x_coordinate = -240
y_coordinate = -100
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    index += 1
    new_turtle.penup()
    new_turtle.goto(x=x_coordinate, y=y_coordinate)
    y_coordinate += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            writer.clear()
            writer.goto(x=0, y=0)
            turtle.penup()
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                writer.write(f"You win! The {winning_color} turtle is now the winner.", align="center",
                             font=("Arial", 16, "bold"))
            else:
                writer.write(f"You lose! The {winning_color} turtle is now the winner.", align="center",
                             font=("Arial", 16, "bold"))

            break

        random_index = random.randint(0, 10)
        turtle.forward(random_index)

my_screen.exitonclick()
