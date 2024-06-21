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
        self.r_score=0
        self.l_score=0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(-280,100)
        self.write(f"score {self.r_score}", align=ALIGN, font=FONT)
        self.goto(280,100)
        self.write(f"score {self.l_score}", align=ALIGN, font=FONT)


    def r_scorenum(self):
        self.r_score +=1
        self.scoreboard()

    def l_scorenum(self):
        self.l_score +=1
        self.scoreboard()

    def loose(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)