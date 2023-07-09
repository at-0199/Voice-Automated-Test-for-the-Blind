                                                                               
from time import time
import speech_recognition as sr  
import os
import playsound
from gtts import gTTS



def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# get audio from the microphone                                                                       
r = sr.Recognizer()

for i in range(2):
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)  


    print(r.recognize_google(audio)) 


