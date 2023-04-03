import math, numpy
import tkinter as tk
from functools import partial
global mode, canvas, points, selected, radio
def select(x, y):
    global canvas, points
    mouse = numpy.array([x, y])
    temp = [9, None]#距離9以上の場合は選択しない
    for i in points:
        dist = numpy.linalg(i - mouse)
        if dist < temp[0]:
            temp[0] = dist
            temp[1] = i
    return temp[1]
def click_canvas(event):
    global mode, canvas, points, selected
    print(event.x, event.y)
    if mode == 0:
        id = canvas.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2)
        points.append((numpy.array([event.x, event.y]), id))
    if mode == 1:
        ret = select(event.x, event.y)
        if ret == None:
            return
        if len(selected) == 0:
            selected.append(ret)
        else:
            canvas.create_line(selected[0][0][0], selected[0][0][1], ret[0][0], ret[0][1])
            selected = []
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
    selected = []
    mode = value

def create_GUI():
    global mode, canvas, points, selected, radio
    selected = []
    points = []
    radio = []
    mode = -1
    root = tk.Tk()
    root.title("GUI")
    root.geometry("600x500")
    root.configure(bg = "white")
    buttons = tk.Frame(root)
    buttons.place(x = 0, y = 0, width = 80, relheight = 1)
    canvas = tk.Canvas(root)
    canvas.place(x = 80, y = 0, relwidth = 1, relheight = 1)
    canvas.configure(bg = "#ffffee")
    canvas.bind(sequence = "<Button-1>", func = click_canvas)
    canvas.bind("<Motion>", move_canvas)
    px_v = tk.IntVar(value = 10)
    radio.append(tk.Radiobutton(buttons, text = "点", value = 0, variable = px_v))
    radio[0]['command'] = partial(click_radio, 0)
    radio[0].place(relx = 0, y = 0, relwidth = 1.0, height = 60)
    radio.append(tk.Radiobutton(buttons, text = "線分", value = 1, variable = px_v))
    radio[1]['command'] = partial(click_radio, 1)
    radio[1].place(relx = 0, y = 60, relwidth = 1.0, height = 60)
    root.mainloop()
eps = 0.001
class point:
    def __init__(self, x, y):
        self.coordinate = (float(x), float(y))
    def angle(self):
        if abs(self) < eps:
            raise ValueError
        return math.atan2(self.coordinate[1], self.coordinate[0])
    def abs(self):
        return (self.coordinate[0] ** 2 + self.coordinate[1] ** 2) ** 0.5
class line:
    def __init__(self, begin: point, direction: point):
        self.begin = begin
        self.direction = direction
class circle:
    def __init__(self, radius: float, center: point):
        self.radius = radius
        self.center = center

def cross(line0, line1):
    outer_product = line0.direction * line1.direction
    if outer_product < eps:
        raise ValueError
    t = -((line0.begin - line1.begin) * line1.direction) / (line0.direction * line1.direction)
    return line0.begin + t * line0.direction


def angle_equisector(line0, line1, n):
    angles = [line0.direction.angle(), line0.direction.angle()]
    origin = cross(line0, line1)
    coeff = 0
    if angles[1] - angles[0] > math.pi:
        coeff += 2 * math.pi
    elif angles[1] - angles[0] < -math.pi:
        coeff -= 2 * math.pi
    ret = set()
    for i in range(1, n):
        ang = (n - i) * angles[0] + i * angles[1]
        ret.add(line(origin, point(math.cos(ang), math.sin(ang))))
    return ret

def circumscribed_circle(points):
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