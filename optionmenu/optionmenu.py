from tkinter import *
win = Tk()
def ok(a):
    l.config(text=var.get())
li = ["c","c++","java"]
var = StringVar()
o = OptionMenu(win,var,*li,command=ok)
var.set("c")
l = Label(win,text="",font=(30))
o.pack()
l.pack()
win.geometry("500x500")
win.mainloop()