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
DELAY = 1

BACKGROUND_COLOR = "black"
HEIGHT = 1000
WIDTH = 1000

def update():
    global stars
    stars2 = []
    for i in stars:
        f = 0
        for j in stars:
            if i != j:
                f += G * i.mass * j.mass / math.sqrt((i.x - j.x) ** 2 + (i.y - j.y) ** 2)
        stars2.append(Star(i.x + f / i.mass, i.y + f / i.mass, i.mass, i.radius))
    stars=stars2
    graphics()
    window.after(DELAY, update)


def graphics():
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

    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth/2) - (windowWidth/2))
    y = int((screenHeight/2) - (windowHeight/2))

    window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

    stars = []

    for i in range(STAR_AMOUNT):
        stars.append(Star(np.random.randint(0, 1000), np.random.randint(0, 1000), np.random.randint(1, 100), np.random.randint(1, 100)))

    update()

    window.mainloop()

