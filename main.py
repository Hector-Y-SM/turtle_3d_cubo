import turtle as t
from tkinter import *

angles = [90, 90, 90, 90, -45, -135, -45, -45, -135, -45, -270, 90, 90, -180, 135]
for x in angles:
    t.right(x)
    t.fd(100)

input('')
