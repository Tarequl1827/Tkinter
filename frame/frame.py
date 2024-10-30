from tkinter import *
win = Tk()
var = LabelFrame(win,text="Hello",font=(30),labelanchor=N)
var1 = Label(win,text="World",font=(30))
win.geometry("800x600")
var.place(x=100,y=100,width=500,height=100)
var1.place(x=110,y=120)
win.mainloop()