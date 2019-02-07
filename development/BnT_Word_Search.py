from tkinter import *
from tkinter import messagebox
import os,re
win = Tk()
win.title('B&T Word Search Tool v1.2')
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
    toBeReplaced =['</span></span>','  </span>',' </span> </span>','  </span></span>',' </span> </span> </span>','-</span> </span>']
    replacewith = ['</span> </span>',' </span>','</span> </span>',' </span></span>',' </span></span></span>','-</span></span>']

    # driving logic.
    for file in directory:
        pathname = os.path.join(fileLOC, file)
        if not os.path.isdir(pathname):
            open_file = open(file,'r',encoding='utf-8')
            read_file = open_file.read()
            if file == 'nav.xhtml':
                # print("nav.xhtml skipped")
                continue
            else:
                for i in range(0,4):
                    try:
                        regex = re.compile(toBeReplaced[i])
                        read_file = regex.sub(replacewith[i], read_file)
                        write_file = open(file,'w',encoding='utf-8')
                        write_file.write(read_file)
                        # print ("processed ", file)
                    except:
                        # print("exception occurred.")
                        messagebox.showinfo("Error", "Exception occurred")                
    # code exit logic.
    messagebox.showinfo("Processed", "Files Processed")

Label(win, text="Text to get").pack()  #label
Entry(win, textvariable = mystring,width=50).pack() #textblock
button = Button(win, text="Proceed", command=getValue) #button
button.pack()
win.geometry("600x300+500+250")
win.mainloop()