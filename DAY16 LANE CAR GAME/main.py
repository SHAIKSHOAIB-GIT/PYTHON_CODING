import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = Cars()
score = Score()


screen.listen()
screen.onkey(player.move, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.movecar()

    # detect collision with cars
    for car in cars.all_cars:
        if car.distance(player)< 25:
            score.game_over()
            game_is_on = False
            
    # detect collision with finish line
    if player.ycor() > 280:
        player.go_to_strat()
        score.level_up()
        cars.LEVEL_UP()





screen.exitonclick()