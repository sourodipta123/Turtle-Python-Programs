from turtle import*
title('Coiling Squares')
bgcolor('black')
pencolor('white')
speed('slow')
width(3)

for i in range(200,20,-20):
    for j in range (2):
        fd(i)
        lt(90)