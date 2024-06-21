from turtle import Turtle

class Lane():
    def __init__(self, position) -> None:
        turtle = Turtle("square")
        turtle.penup()
        turtle.goto(position)
        turtle.setheading(90)
        turtle.shapesize(stretch_len=35, stretch_wid= 1)
        
