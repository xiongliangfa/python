from os import path
from pydub import AudioSegment

# files                                                                         
src = "aud1.mp3"
dst = "aud2.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")