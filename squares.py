import turtle
import random
def random_color():
    colvar=random.randint(0,10)
    L=['red','blue','green','yellow','black','pink','gold','violet','coral','lemon chiffon','sea green']
    result=L[colvar]
    return result

def square(color,x,y):     
     turtle.color(color)
     turtle.begin_fill()
     turtle.penup()
     turtle.goto(x,y)
     turtle.pendown()
     line1=200           #creates a new smaller square
     while line1>=10:   
      line1=line1-10
      for i in range(2):
          turtle.forward(line1)
          turtle.right(90)
          turtle.forward(line1)
          turtle.right(90)

def drawsqr():
    num=5               
    for i in range(num):  
              color=random_color()  #change color after each complete cycle
              x=250
              y=250
              square(color,x,y)