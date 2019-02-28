import speech_recognition as sr
import subprocess
import wave,os
import pydub
from tkinter import *
from tkinter import messagebox
import tkinter as tk

# global deceleration
sox = 'C:/Program Files (x86)/sox-14-4-2/sox.exe'
file_list = []
win = Tk()
win.title('Audio Merge tool V2.1 - HMH')
mystring = StringVar()
audioLabel = StringVar()
countLabel = StringVar()

#func to merge the audio
def mergeAudio(aud1,aud2,outputAudio):
    infiles = [aud1, aud2]
    outfile = outputAudio
    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()

# func for converting audio to text
def SpeechToText(audioName,k): 
    r = sr.Recognizer()
    harvard = sr.AudioFile(audioName)
    with harvard as source:
        audio = r.record(source)
        type(audio)
        try:
            convertedText = r.recognize_google(audio)
            # print(convertedText)
        except:
            convertedText = 'test' + str(k)
        outAudioName = convertedText + '.wav'
        return outAudioName

# adding files to array
def addToArray(filePath):
    file_list.clear()
    directory = os.listdir(filePath)
    os.chdir(filePath)
    for file in directory:
        file_list.append(file)

#  adding silence
def addSilence(aud1):
    infiles = [aud1, 'silence\\silence.wav']
    outfile = aud1
    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()

# mp3 to wav function
def toWav(filePath):
    for i in range(0,len(file_list)):
        audioName = os.path.splitext(file_list[i])[0]
        if not file_list[i] == 'process':
            infile = filePath + '\\' + audioName + '.mp3'
            outfile = filePath + '\\process\\' + audioName + '.wav'
            extra = '--rate 16k --bits 16 --channels 1'
            command = """{0} "{1}" {2} "{3}" """.format(sox,infile,extra,outfile)
            subprocess.call(command)

# wav to mp3 function
def tomp3(filePath):
    for i in range(0,len(file_list)):
        if not file_list[i] == 'silence' or file_list[i] == 'log.txt':
            audioName = os.path.splitext(file_list[i])[0]
            infile = filePath + '\\process\\' + audioName + '.wav'
            outfile = filePath + '\\' + audioName + '.mp3'
            command = """{0} "{1}" "{2}" """.format(sox,infile,outfile)
            subprocess.call(command)

# triggering function
def trigger():
    filePath = mystring.get()  
    addToArray(filePath)
    toWav(filePath) #yet to be implemented
    os.chdir(filePath + "\\process")
    addToArray(filePath + "\\process")
    file = open('log.txt','w')
    for i in range(0,len(file_list),2):
        if not file_list[i] == 'silence':
            win.update_idletasks()
            outputAudio = SpeechToText(file_list[i],i)
            #addSilence(file_list[i])
            mergeAudio(file_list[i],file_list[i+1],outputAudio)
            file.write(file_list[i] + ' + ' + file_list[i+1] +' --> ' + outputAudio + '\n')
    file.close()
    addToArray(filePath + "\\process")
    tomp3(filePath) #yet to be implemented
    messagebox.showinfo("Processed", "Files Processed")

if __name__ == "__main__":
    audioLabel.set('Audio to be generated')
    countLabel.set('0')
    Label(win, text="").pack()  #label
    Label(win, text="Enter Audio Path", justify=LEFT).pack()  #label
    Entry(win, textvariable = mystring,width=50).pack() #textblock
    button = Button(win, text="Proceed", command=trigger) #button
    button.pack()
    win.geometry("350x150+500+250")
    win.mainloop()