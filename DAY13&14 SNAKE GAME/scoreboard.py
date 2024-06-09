from turtle import Turtle
ALIGN ="center"
FONT =("Arial", 25, "normal")

class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("White")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"SCORE : {self.score}", align=ALIGN, font=FONT)

    def loose(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)


    def scorenum(self):
        self.score +=1
        self.clear()
        self.scoreboard()