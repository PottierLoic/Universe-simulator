# galaxy gravitation simulator
# Author : Loïc Pottier
# Date : 29/01/2022

# IMPORTS
from tkinter import *
import numpy as np
import math
import copy

# FILES IMPORTS
from star import Star

# CONSTANTS
G = 6.67408 * 10 ** -11
STAR_AMOUNT = 100
DELAY = 50

BACKGROUND_COLOR = "black"
HEIGHT = 1000
WIDTH = 1000

# TODO: fix the bug where the stars are moving in the wrong direction
def update():
    global stars
    stars2 = []
    for i in stars:
        f = []
        for j in range(len(stars)):
            if i == stars[j]:
                f.append([0, [0, 0]])
                f[j][0] = 0
                f[j][1] = [0, 0]
                j+=1
            else:
                f.append([0, [0, 0]])
                #calculate the force
                f[j][0] = G * i.mass * stars[j].mass / math.sqrt((i.x - stars[j].x) ** 2 + (i.y - stars[j].y) ** 2)
                #calculate the direction
                f[j][1][0] = i.x - stars[j].x 
                f[j][1][1] = i.y - stars[j].y

        
        newx = i.x
        newy = i.y
        for k in range(len(f)):
            #calculate the new position
            a = f[k][1][0]
            b = f[k][1][1]
            newx -= a * f[k][0]
            newy -= b * f[k][0]
    
        #create the new star
        stars2.append(Star(newx, newy, i.mass, i.color))
        
    stars=stars2
    graphics()
    window.after(DELAY, update)

def graphics():
    print("graphics")
    canvas.delete("all")
    for i in stars:
        canvas.create_oval(i.x, i.y, i.x + 5, i.y + 5, fill=i.color)
    window.after(DELAY, graphics)

if __name__ == "__main__":

    window = Tk()
    window.title("Galaxy simulation")

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
    canvas.pack()

    window.update()

    stars = []

    for i in range(STAR_AMOUNT):
        stars.append(Star(np.random.randint(0, 1000), np.random.randint(0, 1000), np.random.randint(5000, 50000), np.random.randint(1, 100)))

    update()

    window.mainloop()

