import math, numpy
import tkinter as tk
from functools import partial
global mode, canvas, points, selected, radio
def find_point(x, y):
    global canvas, points
    mouse = numpy.array([x, y])
    temp = [9, None]#距離9以上の場合は選択しない
    for i in points:
        dist = numpy.linalg.norm(points[i] - mouse, ord = 1)
        if dist < temp[0]:
            temp[0] = dist
            temp[1] = i
    return temp[1]
def select(id):
    global selected, canvas
    canvas.itemconfigure(id, fill = "white")
    selected.append(id)
def select_clear():
    global selected
    for id in selected:
        canvas.itemconfigure(id, fill = "black")
    selected = []
def click_canvas(event):
    global mode, canvas, points, selected
    print(event.x, event.y)
    if mode == 0:
        id = canvas.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill = "black")
        points[id] = numpy.array([event.x, event.y])
    if mode == 1:
        ret = find_point(event.x, event.y)
        if ret == None:
            return
        select(ret)
        if len(selected) == 2:
            canvas.create_line(points[selected[0]][0], points[selected[0]][1], points[selected[1]][0], points[selected[1]][1])
            select_clear()
def move_canvas(event):
    pass
    """
    global mode, canvas, points, selected
    mouse = numpy.array([event.x, event.y])
    temp = [float('inf'), None]
    for i in points:
        dist = numpy.linalg(i - mouse)
        if dist < temp[0]:
            temp[0] = dist
            temp[1] = i
    if temp[1] != None:
        temp[1] = 
    """
def click_radio(value):
    global mode, selected
    select_clear()
    mode = value
def init_globals():
    global mode, points, selected, radio
    mode = -1
    selected = []
    points = {}
    radio = []
def create_GUI():
    A = []
    b = []
    for p in points:
        A.append(list(p.coordinate) + [1.0])
        b.append(-p.abs() ** 2)
    A = numpy.array(A)
    b = numpy.array(b)
    x = numpy.linalg.solve(A, b)
    radius = x[1] ** 2 / 4 + x[0] ** 2 / 4 - x[2]
    if radius < 0:
        raise ValueError
    return circle(radius ** 0.5, point(-0.5 * x[0], -0.5 * x[1])) 
create_GUI()