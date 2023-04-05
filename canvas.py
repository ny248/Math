import math, numpy
import tkinter as tk
from functools import partial
global canvas, command, root, objects, timestamp

class object_base:
    global canvas, timestamp
    def __init__(self, x, y):
        add_object(self)
        self.timestamp = timestamp
        timestamp += 1
        self.deleted = False
    def place(self, pos):
        item = tk.Label(shelf, text = self.place_string(), bd = 2, relief = tk.RAISED)
        item.place(x = 0, y = pos * 40, relwidth = 1, height = 40)
    def __del__(self):
        if id in self:
            canvas.delete(self.id)
        draw_shelf()

class point:
    global canvas, objects, shelf, timestamp
    def __init__(self, x, y):
        super.__init__()
        self.coordinate = (x, y)
        draw_shelf()
    def draw(self):
        x, y = self.coordinate[0], self.coordinate[1]
        self.id = canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill = "black")
    def place_string(self, pos):
        return "point\n" + str(self.timestamp) + " (" + str(self.coordinate[0]) + "," + str(self.coordinate[1]) + ")"

class variable:
    global canvas, objects, shelf, timestamp
    def __init__(self, value = 0):
        super.__init__()
        self.value = value
        draw_shelf()
    def place_string(self, pos):
        return "variable\n" + str(self.timestamp) + " " + str(self.value)

def add_object(obj):
    global timestamp
    objects.append(obj)
    timestamp += 1

def draw_shelf():
    global shelf, timestamp
    for child in shelf.winfo_children():
        child.destroy()
    pos = 0
    for i in range(timestamp):
        if objects[i].deleted == False:
            objects[i].place(pos)
            pos += 1
    
def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

def enter_command(event):
    global command, objects
    exec(command.get())
    print(objects)
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
