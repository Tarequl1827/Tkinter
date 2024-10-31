from tkinter import *
win = Tk()
def python():
    l.config(text="Bangladesh")
btn = Button(win,text="ON",font=(30),relief="flat",bg="red",command=python)
l = Label(win,text="Hello",font=(30))
btn.place(x=100,y=100)
l.place(x=100,y = 200)
win.mainloop()