import math, numpy
import tkinter as tk
from functools import partial
global canvas, command, root
def enter_command(value):
    global command
    print(command.get())

def create_GUI():
    global canvas, command, root
    root = tk.Tk()
    root.title("GUI")
    root.geometry("600x500")
    root.configure(bg = "white")
    objects = tk.Frame(root)
    objects.place(x = 0, y = 0, width = 80, relheight = 0.95)
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