from turtle import Turtle, Screen
import random as r

t = Turtle()
screen = Screen()

screen.colormode(255)
# for _ in range(10):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


# for shape_sides in range(3, 25):
#     t.pencolor((r.randint(1, 256), r.randint(1, 256), r.randint(1, 256)))
#     for _ in range(shape_sides):
#         t.right(360 / shape_sides)
#         t.forward(100)

direction = [0, 45, 90, 135, 180, 225, 270, 315]


def random_color():
    red = r.randint(0, 255)
    g = r.randint(0, 255)
    b = r.randint(0, 255)
    return red, g, b


print(random_color())


# for _ in range(3000):
#     t.pencolor(random_color())
#     t.pensize(10)
#     t.speed("fastest")
#     t.hideturtle()
#     turn = r.choice(direction)
#     t.setheading(turn)
#     t.forward(20)

t.speed("fastest")


def move(degree):
    angle = 0
    t.width(5)
    degree = 360 / degree
    for heading in range(int(360 / degree)):
        t.pencolor(random_color())
        t.circle(100)
        angle += degree
        t.setheading(angle)


move(4)



screen.exitonclick()
















