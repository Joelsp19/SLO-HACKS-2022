from tkinter import *
from FallingStars import *

window = Tk(className = 'Multitask Game')
window.geometry("1500x800")
myCanvas = Canvas(window, width= 1500, height = 800)
myCanvas.pack()



fallinggame = FallingStars(myCanvas)
fallinggame.create_circle(1300, 100, 10)
window.mainloop()

