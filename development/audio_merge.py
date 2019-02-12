from pydub import AudioSegment
import os
print('Enter the directory')
filePath = input(">")
os.mkdir('output')
os.chdir(filePath)
sound = AudioSegment.from_mp3("aud1.mp3")
sound.export("output/aud1.wav", format="wav")