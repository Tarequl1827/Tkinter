# pack(padding) layout management

import tkinter as tk
from tkinter import Label

win = tk.Tk()
win.config(bg="yellow")
l = Label(win,text="Hello bangladesh \nWorld",font=("arial",50,"bold"),fg="white",bg="yellow",relief="sunken",cursor="plus",justify="left")
l.pack(ipadx=100,ipady=100,fill="x",side="right")
win.mainloop()

# grid(table) layout management

import tkinter as tk
from tkinter import Label

win = tk.Tk()
win.config(bg="yellow")
l = Label(win,text="Hello bangladesh \nWorld",font=("arial",50,"bold"),fg="white",bg="yellow",relief="sunken",cursor="plus",justify="left")
l.grid(ipadx=100,ipady=100,padx=100,pady=100)
win.mainloop()

# place(coordinate) layout management

import tkinter as tk
from tkinter import Label

win = tk.Tk()
win.config(bg="yellow")
l = Label(win,text="Hello bangladesh \nWorld",font=("arial",50,"bold"),fg="white",bg="yellow",relief="sunken",cursor="plus",justify="left")
l.place(x=100,y=100,width=100,height=100)
win.mainloop()