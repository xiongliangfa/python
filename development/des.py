import os,re
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # print("allFiles", allFiles)
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            print(fullPath)
            if not re.match("([.a-z])",entry):
                allFiles = allFiles + getListOfFiles(fullPath)
                print(fullPath)
        else:
            allFiles.append(fullPath)
            print(fullPath)
                
    return allFiles
print("Path")
dirName = input("> ")

# Get the list of all files in directory tree at given path
getListOfFiles(dirName)
