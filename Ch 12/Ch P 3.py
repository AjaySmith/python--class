import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=400)
canvas.pack()
girl = PhotoImage(file='c:\\Pic.gif')
canvas.create_image(0, 0, anchor=NW, image=girl)

for x in range(0, 80):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)
