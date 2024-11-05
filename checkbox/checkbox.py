from tkinter import *

win = Tk()
def value():
    l.config(text=var.get())
var = StringVar()
a = Checkbutton(win,text="sports",variable=var,onvalue="Python",offvalue="Java")
btn = Button(win, text="submit",command=value)
l = Label(win,text="Hello",font=(30))
a.pack()
btn.pack()
l.pack()
win.mainloop()

from tkinter import *

win = Tk()
def value():
    l.config(text=var.get())
var = StringVar()
a = Checkbutton(win,text="sports",variable=var,onvalue="Python",offvalue="Java",command=value)
a.deselect()
l = Label(win,text="check",font=(30))
a.pack()
l.pack()
win.mainloop()