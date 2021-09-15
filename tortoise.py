from turtle import Turtle

class Tortoise(Turtle):

    def __init__(self):
        super().__init__()
        self.start_pos = (0, -280)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(self.start_pos)
        self.setheading(90)

    def move(self):
        self.forward(10)
    
    def reset_pos(self):
        self.goto(self.start_pos)