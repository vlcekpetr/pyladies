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

for i in range(4):
    left(90)
    forward(100)
    right(90)
    forward(100)
    
exitonclick()