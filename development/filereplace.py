import os, re
print("Directory-path")
filePath = input(">")
re.sub
fileLOC = filePath.replace("\\\\","\\")
directory = os.listdir(fileLOC)
os.chdir(fileLOC)
# print('Find: ')
# toBereplaced = input('> ')
# print('Replace: ')
# replaceWith = input('> ')
toBereplaced =['  </span>',' </span> </span>','  </span></span',' </span> </span> </span>']
replacewith = [' </span>','</span> </span>',' </span></span>',' </span></span></span>']

# driving logic.
for file in directory:
    pathname = os.path.join(fileLOC, file)
    if not os.path.isdir(pathname):
        open_file = open(file,'r',encoding='utf-8')
        read_file = open_file.read()
        if file == 'nav.xhtml':
            print("nav.xhtml skipped")
        else:
            for i in range(0,4):
                regex = re.compile(toBereplaced[i])
                read_file = regex.sub(replacewith[i], read_file)
                write_file = open(file,'w')
                write_file.write(read_file)
                print ("processed ", file)
# code exit logic. test
input("Press enter key to exit.")