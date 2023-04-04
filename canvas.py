import math, numpy
import tkinter as tk
from functools import partial
global canvas, command, root, objects

class point:
    global canvas, object
    def __init__(self, x, y):
        self.coordinate = (x, y)
        id = canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill = "black")
        objects.add(id)
        draw_shelf()
def draw_shelf():
    global shelf
def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

def enter_command(event):
    global command, objects
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
def create_GUI():
    global canvas, command, root, objects, shelf
    objects = set()
    root = tk.Tk()
    root.title("GUI")
    root.geometry("600x500")
    root.configure(bg = "white")
    shelf = tk.Frame(root)
    shelf.place(x = 0, y = 0, width = 80, relheight = 0.95)
    canvas = tk.Canvas(root)
    canvas.place(x = 80, y = 0, relwidth = 1, relheight = 0.95)
    canvas.configure(bg = "#ffffee")
    #canvas.bind(sequence = "<Button-1>", func = click_canvas)
    #canvas.bind("<Motion>", move_canvas)
    command = tk.Entry()
    command.place(x = 0, rely = 0.95, relwidth = 1, relheight = 0.05)
    command.bind('<Return>', enter_command)
    root.mainloop()
create_GUI()
