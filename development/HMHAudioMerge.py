import speech_recognition as sr
import subprocess
import wave,os
#func to merge the audio
def mergeAudio(outputAudio):
    infiles = ["aud1.wav", "aud2.wav"]
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
def SpeechToText(audioName):
    r = sr.Recognizer()
    harvard = sr.AudioFile(audioName)
    with harvard as source:
        audio = r.record(source)
        type(audio)
        convertedText = r.recognize_google(audio)
        outAudioName = convertedText + '.wav'
        return outAudioName

# func to convert mp3 to wav
def toWav():
    os.chdir('D:\\PYTHON\\python\\test\\audio')
    subprocess.call(['ffmpeg', '-i', '/input/aud1.mp3','/output/aud1.wav'])

        
if __name__ == "__main__":
    toWav()
    pass
    print("enter the audio name")
    audioName = input('> ')
    outputAudio = SpeechToText(audioName)
    mergeAudio(outputAudio)
