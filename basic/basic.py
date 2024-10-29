#basic ui design
import tkinter as tk
win = tk.Tk()
win.mainloop()

#title set
import tkinter as tk
win = tk.Tk()
win.title("Title")
win.mainloop()

#icon set
import tkinter as tk
win = tk.Tk()
win.iconbitmap(r"C:\Users\USER\PycharmProjects\practice\image.ico")
win.mainloop()

#icon and title set
import tkinter as tk
win = tk.Tk()
win.title("Title")
win.iconbitmap(r"C:\Users\USER\PycharmProjects\practice\image.ico")
win.mainloop()

#opacity
import tkinter as tk
win = tk.Tk()
win.attributes("-alpha",0.5)
win.mainloop()

#background color
import tkinter as tk
win = tk.Tk()
win.config(bg="red")
win.mainloop()

#background color
import tkinter as tk
win = tk.Tk()
win["bg"] = "yellow"
win.mainloop()

#background color and opacity
from tkinter import *
win = Tk()
win.config(bg="red")
win.attributes("-alpha",0.5)
win.mainloop()

#size
import tkinter as tk
win = tk.Tk()
win.geometry('300x500')
win.mainloop()

#postion and size
import tkinter as tk
win = tk.Tk()
win.geometry('300x500+100+100')
win.mainloop()

#postion center
import tkinter as tk
win = tk.Tk()
width = 300
height = 500
set_width = win.winfo_screenwidth()
set_height = win.winfo_screenheight()
c_x = int((set_width/2)-(width/2))
c_y = int((set_height/2)-(height/2))
win.geometry(f"{width}x{height}+{c_x}+{c_y}")
win.mainloop()

#minumum and maximum size
import tkinter as tk
win = tk.Tk()
win.minsize(500, 500)
win.maxsize(800,600)
win.geometry('500x500+100+100')
win.mainloop()

#resize stop
import tkinter as tk
win = tk.Tk()
win.resizable(False,False)
win.mainloop()