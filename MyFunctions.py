import turtle
import random
bob=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("light blue")
def jump (x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
def polygon (sides,length,color):
    angle=360/sides
    bob.begin_fill ()
    bob.pencolor(color)
    for num in range (sides):
        bob.forward(length)
        bob.left(angle)
    bob.end_fill() 

# Sun design
def sun(x,y):
  jump(x,y)
  bob.pensize(10)
  bob.color("yellow")
  for times in range(10):
    polygon(3,20,"yellow")
    bob.forward(30)
    bob.right(36)
  jump(16 + x,-75 + y)
  bob.pensize(20)
  bob.circle(30)



# Rainbow   =========================
def rainbow(x,y):
  jump(x,y)
  bob.width(20)
  bob.color("red")
  bob.left(90)
  bob.circle(-60, 180)
  # circle with neg radius = clockwise
  # circle with 2nd value = arc (180 is semi-circle)
  
  jump(x,y)
  bob.setheading(0) # sets turtle direction
  bob.penup()  
  bob.forward(10)
  bob.pendown()
  bob.left(90)
  bob.color("orange")  
  bob.circle(-50, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(20)
  bob.pendown()
  bob.left(90)
  bob.color("yellow")
  bob.circle(-40, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(30)
  bob.pendown()
  bob.left(90)
  bob.color("green")
  bob.circle(-30, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(40)
  bob.pendown()
  bob.left(90)
  bob.color("blue")
  bob.circle(-20, 180)
  
  jump(x,y)
  bob.setheading(0)
  bob.penup()
  bob.forward(50)
  bob.pendown()
  bob.left(90)
  bob.color("purple")
  bob.circle(-10, 180)

# plus sign   =========================
def plus(c,distance):
  bob.color(c)
  bob.width(10)
  for times in range(4):
    bob.forward(distance)
    bob.left(90)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(90)
    
