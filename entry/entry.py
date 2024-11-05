from tkinter import *
win = Tk()
def ok():
    l.config(text=var.get())
var = StringVar()
e = Entry(win,font=(30),show="*",textvariable=var)
b = Button(win,text="show",command=ok)
l = Label(win,text="",font=(30))
e.pack()
b.pack()
l.pack()
win.geometry("500x500")
win.mainloop()