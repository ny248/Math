import math, numpy
import tkinter as tk
from functools import partial
global mode


def click_button_0(button):
    global mode
    if mode != 0:
        mode = 0
        button.config(text = "●点")
    else:
        mode = -1
        button.config(text = "点")

def create_GUI():
    global mode
    mode = -1
    root = tk.Tk()
    root.title("GUI")
    root.geometry("600x500")
    root.configure(bg = "white")
    buttons = tk.Frame(root)
    buttons.place(x = 0, y = 0, width = 80, relheight = 1)
    point_btn = tk.Button(buttons, text = "点")
    point_btn['command'] = partial(click_button_0, point_btn)
    point_btn.place(relx = 0, rely = 0, relwidth = 1.0, relheight = 0.1)
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