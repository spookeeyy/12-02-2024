from turtle import *
 

def hulknurk(n, külg):    
    i = 0
    nurk = 360 / n         
    while (i < n):
        forward(külg)
        left(nurk)
        i = i + 1
 
fillcolor("dark green")
begin_fill()
hulknurk(7, 400)           
end_fill()
 
fillcolor("red")
begin_fill()
hulknurk(5, 50)
move(forward)
end_fill()
 
exitonclick()