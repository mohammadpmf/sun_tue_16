# from turtle import *
# speed(0)
# x=50
# up()
# goto(-4*x,-4*x)
# down()
# for k in range(4):
#     for j in range(4):
#         for i in range(4):
#             fd(x)
#             lt(90)
#         fd(x)
#         begin_fill()
#         for i in range(4):
#             fd(x)
#             lt(90)
#         end_fill()
#         fd(x)
#     fd(-8*x)
#     lt(90)
#     fd(x)
#     rt(90)
#     for j in range(4):
#         begin_fill()
#         for i in range(4):
#             fd(x)
#             lt(90)
#         end_fill()
#         fd(x)
#         for i in range(4):
#             fd(x)
#             lt(90)
#         fd(x)
#     fd(-8*x)
#     lt(90)
#     fd(x)
#     rt(90)
# done()


from turtle import *
speed(0)
x=50
up()
goto(-4*x,-4*x)
down()
for k in range(8):
    for j in range(8):
        begin_fill()
        for i in range(4):
            fd(x)
            lt(90)
        fd(x)
        if (j+k)%2==1:
            end_fill()
    fd(-8*x)
    lt(90)
    fd(x)
    rt(90)
done()