#Bouncing ball

#Plan:
#-Tkinter
#-Draw a Circle
#-Ball class
#-Make it bounce

#multiball

from tkinter import *
from ball import Ball
import random

class App():
    def __init__(self, width, height):
        self.root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.balls = []
        self.create_balls(12)

        self.animate()
        self.root. mainloop()

    def animate(self):
        for ball in self.balls:
            self.check_collision(ball)
            ball.move()
        self.canvas.after(5, self.animate)

    def check_collision(self, ball):
        coords = ball.get_coord()

        if coords["x"] >= self.width - ball.size//2:
            ball.dx = -ball.dx

        if coords["y"] >= self.height - ball.size//2:
            ball.dy = -ball.dy

        if coords["y"] <= 0:
            ball.dy = -ball.dy

        if coords["x"] <= 0:
            ball.dx = -ball.dx

    def create_balls(self, num):
        for i in range(num):
            x = random.random() * self.width
            y = random.random() * self.height
            self.balls.append(Ball(self.canvas, x, y, 10))


game = App(500, 300)
