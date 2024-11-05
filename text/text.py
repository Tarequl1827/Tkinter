from tkinter import *
win = Tk()
def ok():
    l.config(text=t.get("1.0","end"))
t = Text(win,font=(30),height=8,width=20)
b = Button(win,text="click",command=ok)
l = Label(win,font=(30),text="")
t.pack()
b.pack()
l.pack()
win.geometry("500x500")
win.mainloop()