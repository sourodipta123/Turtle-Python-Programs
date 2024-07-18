from turtle import*
title('Cube')
bgcolor('black')
pencolor('white')
width(3)
speed('slowest')

#Use Fuctions

def cube():
    def square(l):
        for i in range(4):
            fd(l)
            lt(90)
        return
    
    square(100)
    lt(30)
    fd(100)
    rt(30)

    square(100)
    lt(90)
    fd(100)
    lt(90+30)
    fd(100)
    rt(30+180)
    fd(100)
    lt(30)
    fd(100)
    rt(90+30)
    fd(100)
    rt(60)
    fd(100)


cube()
