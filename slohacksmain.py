from tkinter import *
from FallingStars import *
from GravityDash import *

window = Tk(className = 'Multitask Game')
window.geometry("1500x800")
c = Canvas(window, width= 1500, height = 800)

fallinggame = FallingStars(c)
fallinggame.create_stars()
window.bind("<Left>", fallinggame.left)
window.bind("<Right>", fallinggame.right)

gGame = GravityDash(c)
gGame.spike_move()
window.bind("<Up>", gGame.up)
window.bind("<Down>", gGame.down)

space = 0
min_space_btwn_spike = 3


def run():
    global space
    gGame.spike_move()
    if (space==0):
        gGame.create_spikes()
        space+=1
    elif (space !=min_space_btwn_spike):
        space+=1
    else:
        space=0

    window.after(200,run)

c.pack()
window.after(1000,run)
window.mainloop()
