from turtle import *
import colorsys
title('Flower Pattern')
bgcolor('black')
tracer(10)
speed('fastest')
title('First Pattern')
def draw():
    h=0
    for i in range (100):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=0.5
        up()
        goto(0,0)
        down()
        color('black')
        speed('fastest')
        fillcolor(c)
        begin_fill()
        rt(98)
        circle(i,12)
        fd(290)
        fd(i)
        lt(29)
        for j in range (129):
            fd(i)
            circle(j,299,2)
        end_fill()
draw()
