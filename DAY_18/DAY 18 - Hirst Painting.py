# import colorgram
# colors = colorgram.extract('h.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle as t
import random

t.colormode(255)

mr_t = t.Turtle()

color_list = [(233, 165, 65), (47, 112, 157), (112, 155, 204), (210, 124, 165), (17, 130, 96), (180, 163, 27),
              (226, 202, 111), (151, 19, 58), (7, 178, 145), (222, 75, 112), (158, 211, 200), (149, 207, 221),
              (171, 45, 89), (226, 81, 42), (25, 32, 81), (119, 174, 125), (40, 166, 202), (121, 108, 160),
              (210, 63, 31), (28, 53, 114), (229, 170, 194), (163, 5, 3), (20, 100, 82), (79, 19, 63),
              (233, 172, 162), (176, 186, 218)]

start_x = -200
start_y = -200
dot_distance = 50

mr_t.penup()
mr_t.speed(0)
for row in range(10):
    for column in range(10):
        mr_t.goto(start_x + column * dot_distance, start_y + row * dot_distance)
        random_color = random.choice(color_list)
        mr_t.dot(20, random_color)

my_screen = t.Screen()
my_screen.exitonclick()
