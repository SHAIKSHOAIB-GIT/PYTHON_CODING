from turtle import Turtle

class Player():
    def __init__(self) -> None:
        self.player()
        
    def player(self):
        turtle = Turtle("turtle")
        turtle.penup()
        turtle.setheading(90)
        turtle.goto((0, -280))

    def left(self):
        new_y = self.xcor() - 20
        self.goto(new_y, self.ycor())

    def right(self):
        new_y = self.xcor() + 20
        self.goto(new_y, self.ycor())
