import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("U.S.A States Game")
image = "blank_states_img.gif"
my_screen.addshape(image)

turtle.shape(image)

score = 0
mr_t = turtle.Turtle()
mr_t.penup()
mr_t.hideturtle()

data = pandas.read_csv("50_states.csv")
states = []

game_over = False

while not game_over:
    answer_state = my_screen.textinput(title=f"{score}/50 States Correct", prompt="Guess a state.").title()
    state_data = data[data.state == answer_state]

    if answer_state == "Exit":
        all_states = data.state.to_list()
        missing_states = []
        for state in all_states:
            if state not in states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn")
        break

    if not state_data.empty and answer_state not in states:
        dx = state_data.x.iloc[0]
        dy = state_data.y.iloc[0]
        mr_t.goto(dx, dy)
        mr_t.write(answer_state, align="center", font=("Calibri", 8, "normal"))
        score += 1
        states.append(answer_state)

    if len(states) == 50:
        game_over = True


# def get_mouse_click_coor(x, y):
#     print(x, y)
# my_screen.onscreenclick(get_mouse_click_coor)
