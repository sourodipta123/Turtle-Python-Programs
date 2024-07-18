from turtle import*
title('Pattern With Circles')
bgcolor('black')
pencolor('white')
speed('fast')

for i in range (30):
    circle(5*i)
    circle(-5*i)
    lt(i)
