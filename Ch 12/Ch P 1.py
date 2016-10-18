from tkinter import *
import random
tk = Tk()
width = 400
height = 400
color = ['red','orange','yellow','green','blue','purple']
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

def rantri():
    P1 = random.randrange(width)
    P12 = random.randrange(height)
    P2 = random.randrange(width)
    P22 = random.randrange(height)
    P3 = random.randrange(width)
    P32 = random.randrange(height)
    c = random.choice(color)
    canvas.create_polygon(P1, P12, P2, P22, P3, P32, \
                          fill=c, outline="black")
        
for x in range(0, 100):
    rantri()
