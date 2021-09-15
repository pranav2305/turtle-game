from turtle import Screen
import turtle
from cars import Cars
from tortoise import Tortoise
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

tortoise = Tortoise()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(tortoise.move, "space")

cars = []
count = 5
game_is_on = True
while game_is_on:
    time.sleep(scoreboard.sleep)
    screen.update()
    for car in cars:
        car.move()
        if tortoise.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if tortoise.ycor() > 280:
        scoreboard.next_level()
        tortoise.reset_pos()
    if count==5:
        cars.append(Cars())
        count=0
    count+=1






screen.exitonclick()