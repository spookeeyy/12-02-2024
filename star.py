from turtle import *


def täht(pikkus, värv):   
    color(värv)
    begin_fill()                 
    i = 0
    while (i < 5):
        fd(pikkus)
        rt(144)
        i = i + 1
    end_fill()
 
täht(500, "black")        
 
exitonclick()