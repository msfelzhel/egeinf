from turtle import * 
tracer(0)
screensize(1024,768)

k = 20 
lt(90)

for i in range(2+1):
    forward(11*k)
    rt(90)
    forward(17*k)
    rt(90)


up()
forward(7*k)
lt(90)
back(1)
rt(90)
down()


for j in range(2+1):
    forward(15*k)
    rt(90)
    forward(7*k)
    rt(90)     

up()

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(5,'blue')

update()
exitonclick()