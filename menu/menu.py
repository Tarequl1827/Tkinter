from tkinter import *
win = Tk()
m = Menu(win)
me = Menu(m,tearoff=0)
me.add_command(label="New")
#sub menu
me1 = Menu(me,tearoff=0)
me1.add_command(label="New")
me1.add_command(label="Copy")
me1.add_command(label="Paste")
me.add_cascade(label="file",menu=me1)


me.add_command(label="Paste")
win.config(menu=m)
m.add_cascade(label="file",menu=me)
m1 = Menu(win)
m2 = Menu(m1,tearoff=0)
m2.add_command(label="Open")
m2.add_command(label="Close")
m.add_cascade(label="Edit",menu=m2)
win.mainloop()