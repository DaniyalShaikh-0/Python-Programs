import turtle
import random
import itertools

COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'pink', 'gold', 'violet', 'orange', 'magenta', 'cyan']

def random_color(iterator=[]):  # intentional dangerous default value
    if not iterator:  # empty container
        colors = COLORS
        random.shuffle(colors)
        iterator.append(itertools.cycle(colors))

    return next(iterator[0])

def rand_col():
    r = random.randrange(0,255,1)
    g = random.randrange(0,255,1)
    b = random.randrange(0,255,1)
    return (r,g,b)

def square(length, x, y):
    (a,b,c)=rand_col()
    turtle.speed(0)
    tup = (a,b,c)
    turtle.colormode(255)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(tup)

    turtle.begin_fill()
    for i in range(9):
        for _ in range(3):
            turtle.begin_fill()
            turtle.color(rand_col())
              # change color after each square
            turtle.pencolor(tup)
            #turtle.right(_)
            turtle.forward(length)
            turtle.right(120)
            turtle.forward(length)
            turtle.right(120)
            turtle.forward(length)
            turtle.end_fill()
        length-=40

square(300, -100, 100)
turtle.exitonclick()