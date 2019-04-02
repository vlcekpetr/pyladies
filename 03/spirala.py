from turtle import forward, left, exitonclick, shape

shape("turtle")


for i in range(360):
    forward(1 + i/36)
    left(5)
    