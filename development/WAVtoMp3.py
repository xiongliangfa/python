import subprocess
sox = 'C:/Program Files (x86)/sox-14-4-2/sox.exe'

infile = 'D:/PYTHON/python/development/aud1.wav'
outfile = 'D:/PYTHON/python/development/aud1.mp3'
#extra = '--rate 16k --bits 16 --channels 1'

command = """{0} "{1}" "{2}" """.format(sox,infile,outfile)
subprocess.call(command)