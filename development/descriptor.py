import os, re
print("Directory-path")
filePath = input(">")
directory = os.listdir(filePath)
os.chdir(filePath)
print("Enter the file path")
# targetFile = input("> ")
#Print Location
def printLoc(Location):
    if os.path.isdir(Location):
        for file in Location:
            pathname = os.path.join(Location, file)
            printLoc(pathname)
    else:
        # write_file = open(targetFile,'w')
        # write_file.append(Location)
        print(Location)
# driving logic.
for file in directory:
    pathname = os.path.join(filePath, file)
    if os.path.isdir(pathname):
        #testcode
        printLoc(pathname)
    elif os.path.isfile(pathname):
        # write_file = open(targetFile,'w')
        # write_file.append(filePath)
        print(pathname)

# code exit logic.
input("Press enter key to exit.")