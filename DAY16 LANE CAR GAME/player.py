from turtle import Turtle

STRATING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.color("Red")
        self.penup()
        self.setheading(90)
        self.go_to_strat()
        
    def move(self):
        self.forward(20)

    def go_to_strat(self):
        self.goto(STRATING_POSITION)
        
        
