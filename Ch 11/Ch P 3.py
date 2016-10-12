import turtle
t = turtle.Pen()

def star(size, points, fill):
    angle = 360 / points
    t.color(0, .6, .4)
    
    if fill == True:
        t.begin_fill()
        
    for x in range(0, points * 2):
        t.forward(size)
        if x % 2 == 0:
            t.left(180 - angle)
        else:
            t.right(180 - (angle * 2))
            
    if fill == True:
        t.end_fill()
        
    for x in range(0, points * 2):
        t.color(0, 0.5, 0)
        t.forward(size)
        if x % 2 == 0:
            t.left(180 - angle)
        else:
            t.right(180 - (angle * 2))
