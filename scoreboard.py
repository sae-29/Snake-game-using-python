from turtle import Turtle
from turtle import *
class score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        data = open("C:\\Users\\HP\\Documents\\python\\python 100 days code challenge\\day 20 and 21 snake game\\data.txt")
        self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(0 , 340)    
        self.write(f"Score = {self.score} High score = {self.high_score}" ,move = True ,align = "center" , font = ("Arial" , 30 , "normal"))
    
    def reset_high_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            data = open("C:\\Users\\HP\\Documents\\python\\python 100 days code challenge\\day 20 and 21 snake game\\data.txt", mode = "w") 
            data.write(f"{self.high_score}")

        self.score = 0
        self.clear()
        self.update_score()    
    # def game_over(self):
    #     self.goto(0,0)    
    #     self.write("Game Over" ,move = True,align = "center"  , font = ("Arial" , 30 , "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()