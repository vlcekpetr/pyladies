
from turtle import shape, left, right, forward, exitonclick, penup, pendown
from math import sqrt

shape("turtle")

left(180)
penup()
forward(100)
left(180)

pendown()
forward(50)
for i in range(18):
    for i in range(4):
        left(90)
        forward(50)
    right(20)
exitonclick()

right(90)
forward(100)
forward(50)
left(90)
for i in range(36):
    left(1)
    forward(1)