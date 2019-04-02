from turtle import shape, left, right, forward, exitonclick, penup, pendown
from math import sqrt

shape("turtle")

left(180)
penup()
forward(300)
left(90)
forward(100)
left(90)
pendown()
for i in range(8):
    left(90)
    forward(60)
    for i in range(2):
        left(150)
        forward(30)
        left(120)
        forward(30)
        left(120)
        forward(30) 
        left(150)
        forward(35)   
    left(180)
    forward(60)
    left(90)
    forward(40)
exitonclick()