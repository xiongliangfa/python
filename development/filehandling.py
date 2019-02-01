import os
import sys
import fileinput
#take input to search
print ("Text to search for:")
textToSearch = input("> ") 

#take input to replace
print ("Text to replace it with:")
textToReplace = input( "> " )

#open file system
print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )
#fileToSearch = 'D:\dummy1.txt'
tempFile = open( fileToSearch, "r+" )

for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        print('Match Found')
        tempFile.write( line.replace( textToSearch, textToReplace ) )
        print('query replace done')
        tempFile.close()
        print('file closed')
    else:
        print('Match Not Found!!')
exit()