from turtle import Turtle ,Screen
from turtle import *

from snake import snake_body
from scoreboard import score_board
from food import Food
import time

snake = snake_body()
food = Food()
scoreboard = score_board()

width = 0.5
height = 0.5
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width , height)
my_screen.title("My snake game .")
my_screen.tracer(0)


my_screen.listen()
my_screen.onkey(fun = snake.up , key = "w")
my_screen.onkey(fun = snake.down , key = "s")
my_screen.onkey(fun = snake.move_r , key = "d")
my_screen.onkey(fun = snake.move_l , key = "a")

is_game_on = True
while is_game_on:
    # this will update the creen when all the segments have move forward then it will update
    my_screen.update()
    #and it will delay by 0.1 second so that our snake will move faster
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 10:
        food.random_location()
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor() > 760 or snake.head.xcor() < -760 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        scoreboard.reset_high_score()
        snake.reset()

    for segments in snake.segment:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10: 
            scoreboard.reset_high_score()





my_screen.exitonclick()