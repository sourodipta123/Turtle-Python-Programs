from turtle import *
title('Rectangle')
bgcolor('black')
pencolor('white')
speed('slowest')
width(3)
#Use of Functions
def rectangle():
    fillcolor('orange')
    begin_fill()
    for i in range(2):
        fd(200)
        lt(90)
        fd(100)
        lt(90)
    end_fill()

#Function Call
rectangle()