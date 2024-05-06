import speech_recognition as sr
# import subprocess

# subprocess.call(['ffmpeg', '-i', 'mp3/incall_22022024_0916_375297928930_375447657648.mp3',
#                  'mp3/incall_22022024_0916_375297928930_375447657648.wav'])

r = sr.Recognizer()
audio_file = sr.AudioFile("mp3/incall_22022024_0916_375297928930_375447657648.wav")

with audio_file as source:
    audio = r.record(source)

text = r.recognize_google(audio, language="ru")
print(text)
with open("text/incall_22022024_0916_375297928930_375447657648.txt", "a") as f:
    print(text, file=f)
