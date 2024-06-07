from turtle import Turtle,Screen

my_turtle = Turtle()
screen = Screen()

def move():
    my_turtle.forward(13)

def back():
    my_turtle.back(13)

def clock():
    my_turtle.right(12)

def anticlock():
    my_turtle.left(12)

def clear():
    screen.clear()
screen.onkey(key="k" ,fun=move) 
screen.onkey(key="s" ,fun=back) 
screen.onkey(key="a" ,fun=clock) 
screen.onkey(key="d" ,fun=anticlock) 
screen.onkey(key="c" ,fun=clear)    

screen.listen()
screen.exitonclick()
   