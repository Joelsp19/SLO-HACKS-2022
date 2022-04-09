import tkinter as tk
import random

class FallingStars:
    def __init__(self, canvasname):
        self.canvas = canvasname
        self.circle = self.create_circle(1300, 100, 10)

    def create_circle(self, x, y, r):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.canvas.create_oval(x0, y0, x1, y1, fill = "green", outline = "black")

    def create_stars(self):
        x = random.randint(0, 400)
        y = x
        print(x)
        #param are (x1, y1) coords of top left, (x2, y2) coords are bottom right
        return self.canvas.create_rectangle(x, 0, x, 20)

    def left(self, event):
        x = -5
        y = 0
        self.canvas.move(self.circle, x, y)

    def right(self, event):
        x = 5
        y = 0
        self.canvas.move(self.circle, x, y)

    def up(self, event):
        x = 0
        y = -5
        self.canvas.move(self.circle, x, y)

    def down(self, event):
        x = 0
        y = 5
        self.canvas.move(self.circle, x, y)
