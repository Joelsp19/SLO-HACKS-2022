from tkinter import *
from FallingStars import *
from gun_game import *

window = Tk(className = 'Multitask Game')
window.geometry("1500x800")
myCanvas = Canvas(window, width= 1500, height = 800)
myCanvas.pack()



fallinggame = FallingStars(myCanvas)
fallinggame.create_stars()
window.bind("<Left>", fallinggame.left)
window.bind("<Right>", fallinggame.right)

window.mainloop()