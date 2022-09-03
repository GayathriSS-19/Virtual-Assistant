#First basic step is speech to text

import speech_recognition as sr

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
listen()        
