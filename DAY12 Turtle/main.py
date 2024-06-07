from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="make your bet",prompt="guess which color trutle wins")
colors=["red","blue","brown","yellow","orange","green"]
y_position = [-100,-60,-20,20,60,100]
all_turtle = []

for turtle_index in range(0,6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(colors[turtle_index])
    my_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(my_turtle)


if user_input:
    race_strat = True

while race_strat:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_strat = False
            winning_color = turtle.pencolor()
            if user_input == winning_color:
                print("you win")
            else:
                print(f"you lose winner is {winning_color} turtle")    
        steps = random.randrange(0,10)
        turtle.forward(steps)




screen.exitonclick()