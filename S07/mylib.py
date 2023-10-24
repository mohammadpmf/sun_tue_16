from turtle import *

def square(size):
    for i in range(4):
        fd(size)
        lt(90)

def rectangle(w, h):
    for i in range(2):
            fd(w)
            lt(90)
            fd(h)
            lt(90)