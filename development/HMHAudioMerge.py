import speech_recognition as sr
import subprocess
import wave,os
import pydub
# global deceleration
file_list = []

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
# def addSilence(aud1):
#     infiles = [aud1, 'silence.wav']
#     outfile = aud1
#     data= []
#     for infile in infiles:
#         w = wave.open(infile, 'rb')
#         data.append( [w.getparams(), w.readframes(w.getnframes())] )
#         w.close()
#     output = wave.open(outfile, 'wb')
#     output.setparams(data[0][0])
#     output.writeframes(data[0][1])
#     output.writeframes(data[1][1])
#     output.close()

if __name__ == "__main__":
    print('Enter the directory')
    filePath = input(">")   
    addToArray(filePath)
    # toWav(filePath)
    file = open('log.txt','w')
    for i in range(0,len(file_list),2):
        outputAudio = SpeechToText(file_list[i],i)
        # addSilence(file_list[i])
        mergeAudio(file_list[i],file_list[i+1],outputAudio)
        print(outputAudio,' Created')
        file.write(file_list[i] + ' + ' + file_list[i+1] +' --> ' + outputAudio + '\n')
    file.close()