from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.sleep = 0.2
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=("Courier", 15, "normal"))
    
    def next_level(self):
        self.level += 1
        self.update()
        self.reduce_sleep()

    def game_over(self):
        self.goto((0,0))
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

    def reduce_sleep(self):
        self.sleep *= 0.9