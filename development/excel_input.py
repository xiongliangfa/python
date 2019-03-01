import openpyxl
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
# gloabl decleration
win = Tk()
win.title("excel test tool")
mystring = StringVar()
inputString = StringVar()

def main():
    excelPath = mystring.get()
    wb_obj = openpyxl.load_workbook(excelPath)
    sheet_obj = wb_obj.active
    cell_obj = sheet_obj.cell(row = 1, column = 1)
    print(cell_obj.value)
    inputstring = inputString.get()
    sheet_obj['C3'].value = inputstring
    wb_obj.save(excelPath) 
    

def fetchFile():
    filename = askopenfilename()
    mystring.set(filename)

if __name__ == "__main__":
    label = Label(win, text = "Excel path")
    label.pack()
    input = Entry(win, textvariable = mystring, width=50)
    input.pack()
    selectFile = Button(win, text="Select file", command = fetchFile)
    selectFile.pack()
    proceed = Button(win, text="Proceed", command=main)
    proceed.pack()
    addContent = Entry(win, textvariable=inputString, width=75)
    addContent.pack()
    win.geometry("350x150+500+250")
    win.mainloop()