# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:34:45 2020
@author: 780020
"""
import turtle

def drawBar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write('  '+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    if height >= 50:
        t.fillcolor("blue")
    elif height < 50 and height >= 30:
        t.fillcolor("yellow")
    else:
        t.fillcolor("red")

xs = [80, 70, 65, 60, 50, 40, 45, 40, 70, 7, 0, 90, 80]

maxheight = max(xs)
numbars = len(xs)
border = 10

bob = turtle.Turtle()
bob.color("blue")
bob.pensize(3)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0-border,0-border,40*numbars+border,maxheight+border)

for a in xs:
    drawBar(bob, a)
wn.exitonclick()