from turtle import Turtle
import random

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.sleep = 0.2
        self.shapesize(stretch_len=2)
        self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.penup()
        self.goto((280, random.randint(-250, 250)))
        self.setheading(180)

    def move(self):
        self.forward(10)
