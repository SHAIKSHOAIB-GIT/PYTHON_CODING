from turtle import Turtle
ALIGN ="center"
FONT =("Arial", 25, "normal")

class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.penup()
        self.goto(-250,270)
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Level : {self.score}", font="Arial", align="left")

    def level_up(self):
        self.score +=1
        self.scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)