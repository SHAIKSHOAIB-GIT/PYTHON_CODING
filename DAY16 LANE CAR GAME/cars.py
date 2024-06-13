from turtle import Turtle
import random
COLOR = ["red", "black", "green", "blue", "grey", "yellow", "pink"]
CARSPEED = 10

class Cars():
    def __init__(self):
        self.all_cars=[]
        self.car_speed = CARSPEED
         
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            new_y = random.randint(-250,250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)


    def movecar(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def LEVEL_UP(self):
        self.car_speed += CARSPEED
        

    
       