from tkinter import *
win = Tk()
x = IntVar(win,value=123)
y = StringVar(win,value="Hello")
z = BooleanVar(win,value=True)
a = DoubleVar(win,value=12.36)
b = StringVar(win)
b.set("World")
c = IntVar()
c.set(456)
d = StringVar(value="Bangladesh")
print(x.get())
print(y.get())
print(z.get())
print(a.get())
print(b.get())
print(c.get())
print(d.get())
win.mainloop()