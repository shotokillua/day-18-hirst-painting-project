# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# #print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
###################################################################################
import turtle as turtle_module
turtle_module.colormode(255)
import random

painting_colors = [
    (198, 12, 32), (250, 237, 17),
    (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
    (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165),
    (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61),
    (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214),
    (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)
]

tam = turtle_module.Turtle()
screen = turtle_module.Screen()
screen.setworldcoordinates(250, 250, -750, -750)

for _ in range(10):
    for _ in range(10):
        tam.speed("fastest")
        tam.hideturtle()
        tam.setheading(180)
        tam.penup()
        tam.forward(50)
        tam.dot(20, random.choice(painting_colors))

    tam.left(90)
    tam.forward(50)
    tam.right(90)
    tam.forward(-500)

screen.exitonclick()