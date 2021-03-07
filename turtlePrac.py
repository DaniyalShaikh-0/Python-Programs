from turtle import  *
import random
def rand_col():
    r = random.randrange(0,255,1)
    g = random.randrange(0,255,1)
    b = random.randrange(0,255,1)
    return (r,g,b)
def col_rand(i):
    colors=['white','violet','indigo', 'blue', 'lightgreen', 'yellow', 'orange','red']
    return colors[7-i]
def circle_():
    speed(0)
    rad = 30
    # circle(50,360,6)
    for _ in  range(7):
        color(col_rand(_))
        begin_fill()
        circle(rad)
        end_fill()
        rad+=20
    done()
def rainbowCirc(height,thick):
    speed(0)
    penup()
    rad = height
    circle(10,90)
    setposition(250,-150)
    for i in range(8):
        pendown()
        begin_fill()
        color(col_rand(i))
        circle(rad,180)
        end_fill()
        penup()
        circle(rad,180)
        rad-=thick
    #setposition(-250,0)
    pendown()
    # color('Black')
    # write('I LOVE YOU SHONI MY LIFE',font=("Arial",30))
    done()
def lines_():
    speed(8)
    forward(200)
    penup()
    setposition(0,-50)
    forward(10)
    pendown()
    forward(180)
    done()
def try_block():
    for i in range(14):
        speed(1)
        color('Black','Red')
        begin_fill()
        seth(240)
        fd(50)
        seth(0)
        fd(50)
        seth(120)
        end_fill()
        color('Black','Yellow')
        begin_fill()
        fd(50)
        seth(0)
        fd(50)
        end_fill()
    seth(240)
    fd(50)
    done()
def sun():    
    color('red', 'yellow')
    begin_fill()
    while True:
        seth(120)
        fd(50)
        lt(90)
        seth(60)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
rainbowCirc(300,20)