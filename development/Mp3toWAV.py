import os
from pydub import AudioSegment

# files
src = "D:/PYTHON/python/development/aud1.mp3"
dst = "D:/PYTHON/python/development/aud1.wav"

val = os.path.isfile(src)
print(val)

val = os.path.isfile(dst)
print(val)

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")