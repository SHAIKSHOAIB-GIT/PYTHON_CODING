import turtle
import random
turtle.colormode(255)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

direction = [0, 90, 180, 270]

my_turtle = turtle.Turtle()
my_turtle.pensize(15)
my_turtle.speed("fastest")

for turtle in range(300):
    my_turtle.color(random_colors())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(direction))