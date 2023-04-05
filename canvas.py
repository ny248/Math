import math, numpy
import tkinter as tk
from functools import partial
global canvas, command, root, objects, timestamp

class object_base:
    global canvas, timestamp
    def __init__(self):
        self.timestamp = timestamp
        add_object(self)
        self.deleted = False
        draw_shelf()
        draw_canvas()
    def place(self, pos):
        item = tk.Label(shelf, text = self.place_string(), bd = 2, relief = tk.RAISED)
        item.place(x = 0, y = pos * 40, relwidth = 1, height = 40)
    def erase(self):
        self.deleted = True
        draw_shelf()
        draw_canvas()

class point(object_base):
    global canvas, objects, shelf, timestamp
    def __init__(self, *definition):
        self.definition = list(definition)
        super().__init__()
    def x(self):
        return eval(self.definition[0])
    def y(self):
        return eval(self.definition[1])
    def draw(self):
        x, y = self.x(), self.y()
        self.id = canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill = "black")
    def place_string(self):
        return "point\n" + str(self.timestamp) + " (" + str(self.x()) + "," + str(self.y()) + ")"

class variable(object_base):
    global canvas, objects, shelf, timestamp
    def __init__(self, *definition):
        self.definition = list(definition)
        super().__init__()
    def value(self):
        return eval(self.definition[0])
    def place_string(self):
        return "variable\n" + str(self.timestamp) + " " + str(self.value())
    
class circle(object_base):
    global canvas, objects, shelf, timestamp
    def __init__(self, *definition):
        self.definition = list(definition)
        super().__init__()
    def radius(self):
        return eval(self.definition[0])
    def center_x(self):
        return eval(self.definition[1])
    def center_y(self):
        return eval(self.definition[2])
    def draw(self):
        x, y, r = self.center_x(), self.center_y(), self.radius()
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r)
    def place_string(self):
        return "circle\n" + str(self.timestamp) + "radius=" + str(self.radius()) + "\ncenter=(" + str(self.center_x()) + "," + str(self.center_y()) + ")"

def add_object(obj):
    global timestamp
    objects.append(obj)
    timestamp += 1

def draw_canvas():
    global canvas, timestamp
    for i in range(timestamp):
        if hasattr(objects[i], "id"):
            tk.delete(objects[i].id)
        if objects[i].deleted == False and hasattr(objects[i], "draw"):
            objects[i].draw()

def draw_shelf():
    global shelf, timestamp
    for child in shelf.winfo_children():
        child.destroy()
    pos = 0
    for i in range(timestamp):
        if objects[i].deleted == False:
            objects[i].place(pos)
            pos += 1

def enter_command(event):
    global command, objects
    S = command.get().split()
    exec(S[0] + "('" + "','".join(S[1:]) + "')")
    """
    com = command.get().split()
    if com[0] == "point":
        if len(com) < 3:
            print("Too few values.")
            return
        pos = []
        for i in range(1, 3):
            if not is_num(com[i]):
                print("Not a number.")
                return
            pos.append(float(com[i]))
        point(pos[0], pos[1])
    else:
        print("Unknown command.")
    """
def create_GUI():
    global canvas, command, root, objects, shelf, items, timestamp
    objects = []
    items = set()
    timestamp = 0
    root = tk.Tk()
    root.title("GUI")
    root.geometry("600x500")
    root.configure(bg = "white")
    shelf = tk.Frame(root)
    shelf.place(x = 0, y = 0, width = 160, relheight = 0.95)
    canvas = tk.Canvas(root)
    canvas.place(x = 160, y = 0, relwidth = 1, relheight = 0.95)
    canvas.configure(bg = "#ffffee")
    #canvas.bind(sequence = "<Button-1>", func = click_canvas)
    #canvas.bind("<Motion>", move_canvas)
    command = tk.Entry()
    command.place(x = 0, rely = 0.95, relwidth = 1, relheight = 0.05)
    command.bind('<Return>', enter_command)
    root.mainloop()
create_GUI()
