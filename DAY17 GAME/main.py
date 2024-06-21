from turtle import Screen
from lane import Lane
from player import Player


screen = Screen()
screen.setup(width= 600, height=600)
screen.tracer(0)
screen.listen()

lanel = Lane((-90, 0))
laner = Lane((90, 0))
player = Player()

screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")



game_is_on = True

while game_is_on:
    screen.update()




screen.exitonclick()