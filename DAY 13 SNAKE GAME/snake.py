from turtle import Turtle
position = [(0, 0),(-20, 0),(-40, 0)]

class Snake:
    def __init__(self):
        self.all_turtle = []

    def create_snake(self):
        for index in position:
            my_turtle = Turtle("square")
            my_turtle.color("white")
            my_turtle.penup()
            my_turtle.goto(index)
            self.all_turtle.append(my_turtle)

    def move(self):       
        # here in range we use start,stop,steps
        for turtle_num in range(len(self.all_turtle)-1, 0, -1):
            new_x = self.all_turtle[turtle_num -1].xcor()
            new_y = self.all_turtle[turtle_num -1].ycor()
            self.all_turtle[turtle_num].goto(new_x, new_y)
        self.all_turtle[0].forward(20)