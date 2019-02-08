#!/usr/bin/python

import tkinter
# import tkMessageBox
import tkinter as tk
top = tkinter.Tk()
#code to add widget will go here

def helloCallBack():
    tk.messagebox.showinfo("Hello Python","dialog box")

B=tkinter.Button(top,text="dialog box", command=helloCallBack)
B.pack()
top.mainloop()
