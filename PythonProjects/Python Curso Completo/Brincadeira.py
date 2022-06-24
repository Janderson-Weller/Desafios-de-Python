from turtle import *

def heart():
    begin_fill()
    pensize(3)
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    end_fill()

def d(): #Função D de Dayane <3
    color('red')
    left(140)
    forward(80)
    right(90)
    forward(30)
    circle(-40, 180)
    forward(30)


color('red', 'pink')
heart()
color('pink')
goto(-30, 60)
d()
done()