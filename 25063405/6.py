from turtle import *
tracer(0)
screensize(1024,768)
k = 15
lt(90)

for i in range(2+1):
    forward(23*k)
    lt(90)
    back(27*k)
    lt(90)
up()
back(5*k)
rt(90)
forward(11*k)
lt(90)
down()
for j in range(2+1):
    forward(26*k)
    rt(90)
    forward(32*k)
    rt(90)    



up()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*k,y*k)
        dot(5,'blue')

update()
exitonclick()