from tkinter import *
win = Tk()
def ok():
    l.config(text=s.get())
s = StringVar()
r = Radiobutton(win,text="male",font=(30),value="male",command=ok,variable=s)
r.deselect()
f = Radiobutton(win,text="Female",font=(30),value="female",command=ok,variable=s)
f.deselect()
l = Label(win,text="",font=(30))
l.pack()
r.pack()
f.pack()
win.mainloop()