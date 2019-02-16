import speech_recognition as sr
import subprocess
import wave,os
import pydub
from tkinter import *
from tkinter import messagebox

# global deceleration
file_list = []
win = Tk()
win.title('Audio Merge tool V2.1 - HMH')
mystring = StringVar()

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
    directory = os.listdir(filePath)
    os.chdir(filePath)
    for file in directory:
        file_list.append(file)

# # adding silence
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

def trigger():
    filePath = mystring.get()  
    addToArray(filePath)
    # toWav(filePath)
    file = open('log.txt','w')
    for i in range(0,len(file_list),2):
        if not file_list[i] == 'silence':
            outputAudio = SpeechToText(file_list[i],i)
            addSilence(file_list[i])
            mergeAudio(file_list[i],file_list[i+1],outputAudio)
            print(outputAudio,' Created')
            file.write(file_list[i] + ' + ' + file_list[i+1] +' --> ' + outputAudio + '\n')
    file.close()

if __name__ == "__main__":
    Label(win, text="Enter Audio Path").pack()  #label
    Entry(win, textvariable = mystring,width=50).pack() #textblock
    button = Button(win, text="Proceed", command=trigger) #button
    button.pack()
    win.geometry("600x300+500+250")
    win.mainloop()
