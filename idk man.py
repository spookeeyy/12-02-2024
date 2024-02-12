from turtle import *

def ruut(joonevärv = "black", täitevärv = "black", külg = 100):
    pencolor(joonevärv)
    fillcolor(täitevärv)
    begin_fill()
    down()
    i = 0
    while i < 4:
        forward(küljepikkus)
        left(90)
        i = i + 1
    end_fill()
    up()
        
def ring(joonevärv = "black", täitevärv = "black", külg = 50):
    pencolor(joonevärv)
    fillcolor(täitevärv)
    down()
    begin_fill()
    circle(raadius)
    up()
    
ruut()
ring()
exitonclick()