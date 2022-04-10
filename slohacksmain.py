from tkinter import *
from FallingStars import *
from GravityDash import *

def setup():
    global J
    global fallinggame
    global gGame
    global Score
    fallinggame = FallingStars(c, window)
    window.bind_all("<KeyPress>", fallinggame.on_keypress)
    window.bind_all("<KeyRelease>", fallinggame.on_keyrelease)

    gGame = GravityDash(c)
    gGame.spike_move()
    window.bind("<Up>", gGame.up)
    window.bind("<Down>", gGame.down)

    Score = 0

    J = c.create_text(1325, 50, text=("Score:", Score), font=("Times New Roman", 50))

    b.pack_forget()

    c.pack()
    window.after(100, run)

window = Tk(className = 'Multitask Game')
window.geometry("1500x800")
c = Canvas(window, width= 1500, height = 800)
b = Button(window, text = "Play", fg = "black", bg = "grey", command = setup, height = 10, width = 15, font = ("Times New Roman", 32))
b.pack(pady = 350)

def change():
    global Score
    global J
    Score+=1
    c.delete(J)
    J=c.create_text(1325,50, text=("Score:", Score), font=("Times New Roman", 50))

space = 0
min_space_btwn_spike = 15

space2 = 0
min_space_btwn_stars = 20

counter = 0

def run():
    #add code for what happens during different games...
    global fallinggame
    global gGame
    global counter
    if counter != 0 and counter % 30 == 0:
        change()
    global space2
    if (space2 == 0):
        fallinggame.create_stars()
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
    counter += 1

window.mainloop()

