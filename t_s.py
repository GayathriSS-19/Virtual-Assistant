#gTTS -->Google Text to Speech

from gtts import gTTS
speech=gTTS("Hello Mahesh Babu,Nice to Meet You")
print(speech)   #gives an object with some byte code

#save it in .mp3 file
a=speech.save('audiot-s.mp3')
