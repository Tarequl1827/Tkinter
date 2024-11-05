from tkinter import *
win = Tk()
menu1 = Menubutton(win,text="File")
menu1.menu = Menu(menu1,tearoff=False)
menu1["menu"] = menu1.menu
menu1.menu.add_checkbutton(label="New file")
menu1.menu.add_checkbutton(label="Open file")
menu1.menu.add_checkbutton(label="Save file")
win.geometry("500x500")
menu1.pack()
win.mainloop()