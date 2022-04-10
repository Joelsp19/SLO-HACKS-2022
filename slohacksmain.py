from tkinter import *
from FallingStars import *
from GravityDash import *

window = Tk(className = 'Multitask Game')
window.geometry("1500x800")
c = Canvas(window, width= 1500, height = 800)

fallinggame = FallingStars(c, window)
window.bind_all("<KeyPress>", fallinggame.on_keypress)
window.bind_all("<KeyRelease>", fallinggame.on_keyrelease)

gGame = GravityDash(c)
gGame.spike_move()
window.bind("<Up>", gGame.up)
window.bind("<Down>", gGame.down)

space = 0
min_space_btwn_spike = 15

space2 = 0
min_space_btwn_stars = 20

counter = 0


def run():
    #add code for what happens during different games...
    global space2
    if (space2 == 0):
        star = fallinggame.create_stars()
        space2 += 1
    elif (space2 != min_space_btwn_stars):
        space2 += 1
    else:
        space2 = 0
    fallinggame.animate_stars()
    if(fallinggame.check_hit()):
        print("YOU SUCK")


    #what happens during Gravity Game
    gGame.spike_move()
    global space
    if (space==0):
        gGame.create_spikes()
        space+=1
    elif (space !=min_space_btwn_spike):
        space+=1
    else:
        space=0
    if(gGame.check_hit()):
        print("Game Over")
    window.after(50, run)

c.pack()
window.after(100,run)
window.mainloop()

