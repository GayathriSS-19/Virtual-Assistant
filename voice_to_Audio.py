#First basic step is speech to text


import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time


#to make sure it listen

def listen():
    r=sr.Recognizer()  #prints the speech as text
    with sr.Microphone() as source:
        print("I am listening")
        audio=r.listen(source,phrase_time_limit=5)
    data=""   #we get attribute error couldnot find the Pi Audio ,soo we will download it using the lfd.uci

#exception Handling
    try:
        data=r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
## Responding
def respond(String):
    print(String)
    tts=gTTS(text=String,lang='en')
    tts.save('speech.mp3')
    playsound.playsound('speech.mp3')
    os.remove('speech.mp3')

def voice_assistant(data):
    """Giving your actions"""
    if "how are you" in data:
        listening =True
        respond("Good and doing well")
    if "time" in data:
        listening=True
        respond(time.ctime())
time.sleep(2)
respond("Hey Gayathri How are you")
listening =True
if listening==True:
    data=listen()
    listening =voice_assistant(data)

