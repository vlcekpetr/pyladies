from turtle import forward, left, exitonclick, shape

shape("turtle")


for i in range(20):
    forward(20 + (i*10))
    left(90)
    
exitonclick()

