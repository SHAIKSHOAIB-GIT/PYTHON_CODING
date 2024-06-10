from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
screen.listen()

ball = Ball()
score = Score()
r_paddle = Paddle((-350, 0))
l_paddle = Paddle((350, 0))


screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision of ball with wall
    if ball.ycor()>290 or ball.ycor() <-290:
        ball.bounce_y()

    # detect collision of ball with paddle
    if ball.distance(l_paddle) < 50 and ball.xcor()> 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x() 

    if ball.xcor()>380:
        ball.reset_position()
        score.r_scorenum()

    if ball.xcor()<-380:    
        ball.reset_position()
        score.l_scorenum()

        
        
screen.exitonclick()