import turtle
import random

turtle.colormode(255)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

my_turtle = turtle.Turtle()
my_turtle.speed("fastest")

def draw_circles(size):
    for draw_circles in range(int(360/size)):
        my_turtle.circle(100)
        my_turtle.color(random_colors())
        my_turtle.setheading(my_turtle.heading() +size)
    
draw_circles(1)
   
    


