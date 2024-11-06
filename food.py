from turtle import Turtle
import random
import snake

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("red")
        self.speed("fastest")
        self.random_location()

    def random_location(self):
        random_x = random.randint(-640 ,640)
        random_y = random.randint(-360 ,360) 
        self.goto(random_x , random_y)    