from turtle import *

def hulknurk(n):
    i = 0
    nurk = 360 / n
    while (i < n):
        forward(100)
        left(nurk)
        i += 1
        
hulknurk(6, 150)
exitonclick()