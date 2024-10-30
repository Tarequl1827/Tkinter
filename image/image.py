from tkinter import *
win = Tk()
var = PhotoImage(file="images.png")
l = Label(win,image=var,text="Only png format support",font=(30),compound="top",pady=20)
win.geometry("600x600")
l.place(x=100,y=100,width=500,height=500)
win.mainloop()