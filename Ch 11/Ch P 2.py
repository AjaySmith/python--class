import turtle
t = turtle.Pen()

def myoct(size, fill):
    if fill == True:
        t.begin_fill()
    for x in range(1, 9):
        t.color(0, 0.7, 1)
        t.forward(size)
        t.left(45)
    if fill == True:
        t.end_fill()
    for x in range(1, 9):
        t.color(0, 1, 0)
        t.forward(size)
        t.left(45)
