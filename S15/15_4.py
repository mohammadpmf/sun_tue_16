from turtle import *

def add(a, b, *args, **kwargs):
    return a+b+sum(args)

print(add(1,2,3))
print(add(1,2,3,4))
print(add(1,2))
print(add(2,2,3,8,65,5,4,3,2,54,6,7,8,9,5,45,3,5,4,44,4,4444, k=5, k2=6))