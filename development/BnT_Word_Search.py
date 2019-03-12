from tkinter import *
from tkinter import messagebox
import os,re

#global declaration
win = Tk()
win.title('B&T Word Search Tool v1.3 - Follett')
mystring = StringVar()


def getValue():
    # address = mystring.get()
    # messagebox.showinfo("Processed",address)
    # print("Directory-path")
    filePath = mystring.get()
    fileLOC = filePath.replace("\\\\","\\")
    directory = os.listdir(fileLOC)
    os.chdir(fileLOC)
    # print('Find: ')
    # toBeReplaced = input('> ')
    # print('Replace: ')
    # replaceWith = input('> ')
    toBeReplaced = ['>READ<','>CHECK MY UNDERSTANDING<','>DRAW<','>IT<','>CHECK<','>MY<','>UNDERSTANDING<','>DRAW IT<','>PROMPT<','>PLAN<','>GENRE<','>STUDY<','>GENRE STUDY<','>MAKE<','>A<','>PREDICTION<','>MAKE A PREDICTION<','>SET<','>A<','>PURPOSE<','>SET A PURPOSE<','>PERFORMANCE TASK<','>PERFORMANCE<','>TASK<','>DRAFT<','>REVISE<','>AND<','>EDIT<','>REVISE AND EDIT<','>PUBLISH<','>PREPARE TO VIEW<','>Respond To The Text<','>WRITE<','>GENRE FOCUS<']
    replacewith = ['>Read<','>Check My Understanding<','>Draw<','>It<','>Check<','>My<','>Understanding<','>Draw It<','>Prompt<','>Plan<','>Genre<','>Study<','>Genre Study<','>Make<','>A<','>Prediction<','>Make A Prediction<','>Set<','>A<','>Purpose<','>Set A Purpose<','>Performance Task<','>Performance<','>Task<','>Draft<','>Revise<','>And<','>Edit<','>Revise And Edit<','Publish','>Prepare To View<','>Respond To The Text<','>Write<','>Genre Focus<']
    # print(replacewith[0])

    # driving logic.
    for file in directory:
        pathname = os.path.join(fileLOC, file)
        if not os.path.isdir(pathname):
            open_file = open(file, 'r', encoding='utf-8')
            read_file = open_file.read()
            if file == 'nav.xhtml':
                print("nav.xhtml skipped")
                continue
            else:
                for i in range(0, len(replacewith)):
                    try:
                        regex = re.compile(toBeReplaced[i])
                        read_file = regex.sub(replacewith[i], read_file)
                        write_file = open(file, 'w', encoding='utf-8')
                        write_file.write(read_file)
                    except:
                        # print("exception occurred.")
                        messagebox.showinfo("Error", "Exception occurred")
        print ("processed ", file)
    # code exit logic.
    messagebox.showinfo("Processed", "Files Processed")


if __name__ == "__main__":
    Label(win, text="Enter OPS path").pack()  #label
    Entry(win, textvariable = mystring, width=50).pack() #textblock
    button = Button(win, text="Proceed", command=getValue) #button
    button.pack()
    win.geometry("600x300+500+250")
    win.mainloop()