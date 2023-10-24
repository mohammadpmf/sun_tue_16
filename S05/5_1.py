from turtle import *

for j in range(4):
    w = numinput("Width", "Enter Width: ")
    h = numinput("Height", "Enter Height: ")
    c = textinput("Color", "Enter Color: ")
    x = numinput("X", "X:")
    y = numinput("Y", "Y:")
    up()
    goto(x, y)
    down()
    fillcolor(c)
    begin_fill()
    for i in range(2):
        fd(w)
        lt(90)
        fd(h)
        lt(90)
    end_fill()
    # name = textinput("Name", "Enter your name: ")
    # write(name, font=('', 26), align='center')


done()