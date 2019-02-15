from pydub import AudioSegment
import os
# global deceleration
file_list = []

def addToArray(filePath):
    directory = os.listdir(filePath)
    os.chdir(filePath)
    for file in directory:
        file_list.append(file)

def Mp3toWAV(audio):
    audioname = os.path.splitext(audio)[0]
    inputStr = audioname + '.mp3'
    outputStr = '/output/' + audioname + '.wav'
    print(AudioSegment.from_mp3(inputStr))
    sound = AudioSegment.from_mp3(inputStr)
    sound.export(outputStr, format="wav")

if __name__ == "__main__":
    print("Enter the directory")    
    filePath = input('> ')
    os.chdir(filePath)
    os.mkdir('output')
    addToArray(filePath)
    for i in range(0,len(file_list),1):
        Mp3toWAV(file_list[i])