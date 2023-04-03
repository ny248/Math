import time
import tkinter
print(tkinter.Tcl().eval('info patchlevel'))
def func1():
   global win
   win = tkinter.Tk()
   win.geometry("300x200")
   win.configure(bg='blue')
   button_win = tkinter.Button(win,text='Go',command=func2)
   button_win.pack()
   win.mainloop()

def func2():
   win.configure(bg = 'green')
   win.update_idletasks()
   time.sleep(5)
   func3()

def func3():
    win.configure(bg = 'yellow')
    win.update_idletasks()

func1() 