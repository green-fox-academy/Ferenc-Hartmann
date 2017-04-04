#Bouncing ball

#Plan:
#-Tkinter
#-Draw a Circle
#-Ball class
#-Make it bounce

from tkinter import *
from ball import Ball

class App():
    def __init__(self, width, height):
        self.dx = 1
        self.dy = 1
        self.root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.ball = Ball(self.canvas, 10, 10, 10)
        self.animate()
        self.root. mainloop()

    def animate(self):
        self.check_collision()
        self.ball.move(self.dx, self.dy)
        self.canvas.after(10, self.animate)

    def check_collision(self):
        coords = self.ball.get_coord()

        if coords["x"] >= self.width - self.ball.size//2:
            self.dx = -self.dx

        if coords["y"] >= self.height - self.ball.size//2:
            self.dy = -self.dy

        if coords["y"] <= 0:
            self.dy = -self.dy

        if coords["x"] <= 0:
            self.dx = -self.dx

game = App(500, 300)
