from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.title("THE SNAKE GAME")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
snake.create_snake()

while True:
    screen.update()
    time.sleep(1)
    snake.move()


    


screen.exitonclick()