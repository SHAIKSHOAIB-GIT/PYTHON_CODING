from turtle import Screen, Turtle
import pandas

turtle = Turtle()
screen = Screen()
screen.title("indian states")
image = "DAY18 INDIA STATES GAME\India-state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("DAY18 INDIA STATES GAME\states_data.csv")
all_states = data.state.to_list()

guess_list = []

while len(guess_list)<30:
    answer = screen.textinput(title=f"{len(guess_list)}/30 states correct", prompt="find all states").title()

    if answer == "Exit":
        break

    if answer in all_states:
        guess_list.append(answer)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
