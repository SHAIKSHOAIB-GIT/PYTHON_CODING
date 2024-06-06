from turtle import Turtle

my_trutle = Turtle()

def draw_shape(n_sides):
    angle = 360 / n_sides
    for i in range(n_sides):
        my_trutle.forward(100)
        my_trutle.right(angle)

for sides in range(3, 10):
    draw_shape(sides)

        
