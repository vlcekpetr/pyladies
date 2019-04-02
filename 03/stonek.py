
from turtle import shape, left, right, forward, exitonclick, penup, pendown
from math import sqrt

shape("turtle")



right(90)
forward(100)
for i in range(4):
    forward(50)
    left(60)
    for i in range(60):
        left(2)
        forward(2)
    right(300)
    for a in range(60):
        left(2)
        forward(2)