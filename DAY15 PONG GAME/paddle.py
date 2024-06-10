from turtle import Turtle
POSITION = [(350, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("White")
        self.penup()
        self.goto(position)  
        

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
            