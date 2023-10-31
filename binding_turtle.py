from turtle import *
color('black')
def change_color1():
    color('red')
def change_color2():
    color('blue')
def change_color3():
    color('green')
def move():
    fd(20)
def lt90():
    lt(90)
def lt5():
    lt(5)
onkey(move, 'a')
onkey(change_color1, 'r')
onkey(change_color2, 'b')
onkey(change_color3, 'g')
onkey(lt90, 'l')
onkey(lt5, 'Left')
listen()
while True:
    fd(1)    
done()