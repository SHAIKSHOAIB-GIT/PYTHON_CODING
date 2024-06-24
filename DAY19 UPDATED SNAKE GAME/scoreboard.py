from turtle import Turtle
ALIGN ="center"
FONT =("Arial", 25, "normal")

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("White")
        self.score = 0
        with open("DAY19 UPDATED SNAKE GAME\data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"SCORE : {self.score} HIGHSCORE: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("DAY19 UPDATED SNAKE GAME\data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.scoreboard()
        

    # def loose(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)


    def scorenum(self):
        self.score +=1
        self.scoreboard()