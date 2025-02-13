import turtle

def dibujar_linea(x1, y1, x2, y2, pasos=100, tamaño=1):
    for i in range(pasos + 1):
        t = i / pasos
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        
        print('x: ', x)
        print('y: ', y)
        
        turtle.penup()
        turtle.goto(x, y)
        turtle.dot(tamaño)
        
turtle.speed(5000)
dibujar_linea(0, -100, 0, 100)
dibujar_linea(-100, -100, -100, 100)
dibujar_linea(-100, 100, 0, 100)
dibujar_linea(0, 100, -100, -100)
dibujar_linea(-100, -100, 0, -100)
input('')
