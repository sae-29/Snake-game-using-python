import time
from turtle import Turtle

turtle_all = [(0,0),(-20,0),(-40,0)]


class snake_body:
    def __init__(self):
            self.segment = []
            self.create_snake()
            self.head = self.segment[0]
            self.extend()
            self.up()
            self.down()
            self.move_r()
            self.move_l()
    
    def create_snake(self):
        for position in turtle_all:
            self.add_segment(position)
            

    def add_segment(self , position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segment.append(new_turtle)

            
    def extend(self):
        self.add_segment(self.segment[-1].position())        

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]


    def move(self):
        for seg_num in range(len(self.segment)-1 , 0 , -1):
                new_x = self.segment[seg_num - 1].xcor()
                new_y = self.segment[seg_num - 1].ycor()
                self.segment[seg_num].goto(new_x , new_y)
        self.head.forward(10)


    def up(self):
    # it checks if the angle is not downward then we can make it move upwards
        if self.head.heading() != 270:
            # setheading() function gives the angle where we wnat to head our snake it takes input as angles
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def move_r(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_l(self):
        if self.head.heading() != 0:
            self.head.setheading(180)    