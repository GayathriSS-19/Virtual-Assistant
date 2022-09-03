#First basic step is speech to text


import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time
import re         #to search while opening a web page
import requests     #to connect to a webpage
import webbrowser   #to open a webpage
import bs4
import smtplib      #to send an email-simple mail transfer protocol


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
    if "open google" in data.casefold():
        listening=True
        # reg_ex=re.search('open google(.*)',data)
        url="https://www.google.com/"
        # if reg_ex:
        #     sub=reg_ex.group(1)
        #     url=url+'r/'
        webbrowser.open(url)
        respond("Done")
    #email gives error as less secure is no longer supported
    # if "email" in data:
    #     listening=True
    #     respond("Whom should I send the mail to")
    #     to=listen()
    #     edict={'hello':"mrygayathri@gmail.com",'just':"gayathrisaisreepolamarasetti@gmail.com"}
    #     toaddr=edict[to]
    #     respond("What is the subject?")
    #     subject=listen()
    #     respond("What should I tell the person?")
    #     message=listen()
    #     content='Subject:{}\n\n{}'.format(subject,message)

    #     #init gmail SMTP
    #     mail = smtplib.SMTP('smtp.gmail.com',587)
    #     #identify the server
    #     mail.ehlo()
    #     mail.starttls()
    #     #login
    #     mail.login('gayathrisaisreepolamarasetti@gmail.com','*Saisri6515')
    #     mail.sendmail('gayathrisaisreepolamarasetti@gmail.com',toaddr,content)
    #     respond("Email sent")

    #webscraping
    if "wiki" in data.casefold():
        listening=True
        url="https://en.wikipedia.org/wiki/"
        respond("What should I Search")
        query =listen()
        response=requests.get(url+query)
        if response is not None:
            html=bs4.BeautifulSoup(response.text,'html.parser')
            paragraphs=html.select('p')
            intro=[i.text for i in paragraphs]
            halo=' '.join(intro)
            respond(halo[:200])
    if "stop" in data:
        listening=False
        print("Listening Stopped")
        respond("See you Gayathri")
    try:
        return listening
    except UnboundLocalError:
        print("Timed out")

#time.sleep(2)
respond("Hey Gayathri How are you")
listening =True
while listening==True:
    data=listen()
    listening =voice_assistant(data)

