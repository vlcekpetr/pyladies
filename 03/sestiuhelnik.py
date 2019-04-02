from turtle import shape, left, right, forward, exitonclick, penup, pendown
from math import sqrt

shape("turtle")

left(180)
penup()
forward(100)
left(180)

pendown()
forward(50)
for i in range(7):
    for i in range(7):
        left(60)
        forward(50)
    right(120)
exitonclick()