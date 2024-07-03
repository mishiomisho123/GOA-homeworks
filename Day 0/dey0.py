from turtle import *


#we want to paint a house

speed(40)
#step 1: draw a spuare

width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)                #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(0, 0)
right(60)
right(90)
forward(200)
right(90)
forward(70)
pendown()
color("black")
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(25)
left(90)
forward(60)
penup()
goto(0, 0)
forward(70)
pendown()
begin_fill()
color("yellow")

left(90)
forward(120)                #height of the door
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
end_fill()
right(90)


penup()
goto(0,0)
pendown()
begin_fill()
color("green")
left(90)
forward(1000)
right(180)
forward(2000)
right(90)
forward(1000)
right(90)
forward(2000)
right(90)
forward(1000)
right(90)
forward(1000)
end_fill()












exitonclick()