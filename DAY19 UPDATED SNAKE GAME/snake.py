from turtle import Turtle
position = [(0, 0),(-20, 0),(-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for index in position:
            self.append_snake(index)


    def append_snake(self, index):
        my_turtle = Turtle("square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(index)
        self.all_turtle.append(my_turtle)

    def extend_snake(self):
        self.append_snake(self.all_turtle[-1].position())

    def reset(self):
        for turtle in self.all_turtle:
            turtle.goto(1000,1000)
        self.all_turtle.clear()
        self.create_snake()
        self.head = self.all_turtle[0]

    def move(self):       
        # here in range we use start,stop,steps
        for turtle_num in range(len(self.all_turtle)-1, 0, -1):
            new_x = self.all_turtle[turtle_num -1].xcor()
            new_y = self.all_turtle[turtle_num -1].ycor()
            self.all_turtle[turtle_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)