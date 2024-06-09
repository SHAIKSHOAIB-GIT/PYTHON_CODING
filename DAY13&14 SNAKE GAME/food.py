from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)


        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed("fastest")
        self.refood()

    def refood(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)    