from turtle import *
 
def ruut(küljepikkus = 100):                
    i = 0
    while i < 4:
        forward(küljepikkus)
        left(90)
        i = i + 1
 
ruut(50)                     
right(45)
ruut(75)
right(45)
ruut()
 
exitonclick()