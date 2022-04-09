import tkinter as tk

class FallingStars:
    def __init__(self, canvasname):
        self.canvas = canvasname

    def create_circle(self, x, y, r):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.canvas.create_oval(x0, y0, x1, y1, fill = "green", outline = "black")