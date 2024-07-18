from turtle import *
title('Square')
bgcolor('Black')
pencolor('White')
width(3)
speed('slowest')
#Using Functions
def Square():
    fillcolor('green')
    begin_fill()
    for i in range(4):
        fd(200)
        lt(90)
    end_fill()

#Function Call
Square()