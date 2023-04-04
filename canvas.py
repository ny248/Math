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
    global canvas, radio
    init_globals()
    root = tk.Tk()
    root.title("GUI")
    root.geometry("600x500")
    root.configure(bg = "white")
    objects = tk.Frame(root)
    objects.place(x = 0, y = 0, width = 80, relheight = 0.95)
    canvas = tk.Canvas(root)
    canvas.place(x = 80, y = 0, relwidth = 1, relheight = 0.95)
    canvas.configure(bg = "#ffffee")
    canvas.bind(sequence = "<Button-1>", func = click_canvas)
    canvas.bind("<Motion>", move_canvas)
    command = tk.Entry()
    command.place(x = 0, rely = 0.95, relwidth = 1, relheight = 0.05)
    root.mainloop()
create_GUI()