import os,re
import unicodedata
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles
print("Path")
dirName = input("> ")
print("Input folder")
targetFile = input('> ')
unicodedata.name(targetFile[0])

# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)
write_file = open(targetFile,'w')
write_file.write(listOfFiles)