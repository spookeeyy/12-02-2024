from turtle import *
 
def silm():                    
    pencolor("#000000")
    fillcolor("red")
    begin_fill()
    circle(25)
    end_fill()
 
pencolor("white")        
fillcolor("black")  
begin_fill()
circle(100)                 
end_fill()
 
up()
bk(45)
lt(90)
fd(100)
rt(90)
down()
 
silm()                     
 
up()                             
fd(90)
down()
 
silm()                    
 
up()                       
bk(95)
rt(90)
fd(30)
down()
circle(50,180)             
bgcolor("dark red")

exitonclick()
print("\n""/n")