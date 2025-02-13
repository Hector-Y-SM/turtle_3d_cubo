from turtle import *
import turtle as t
from tkinter import *

t.hideturtle()  #no turtugaaaaaaaaaaaaaaaaaaa
pu()


def draw_line(steps):
    for x in range(steps):
        t.dot(3)
        goto(x, x + 2)
        #t.right(90)
        t.dot(3)  


draw_line(100)


input('')