from re import I
import pyttsx3
import requests
from sqlalchemy import false
from snapshots import *
import speech_recognition as sr  
import playsound
from listen import *
from test import *

# initialisation
engine = pyttsx3.init()

def mcq_for_test():
    response = requests.get("https://my-json-server.typicode.com/markaashish/Voice_test/db")
    data = response.json()["questions"]
    import time


    c_answers = []
    answers = []


    for i in data:
        c_answers.append(str(i["correct_answer"]))

    i=0

    while(i<len(data)):
        #c_answers.append(str(data[i]["correct_answer"]))
        speak(str(data[i]["question"]))
        speak("A " + str(data[i]["answers"]["a"]))
        speak("B " + str(data[i]["answers"]["b"]))
        speak("C " + str(data[i]["answers"]["c"]))
        speak("D " + str(data[i]["answers"]["d"]))
        speak("..." + str(data[i]["answers"]["e"]))
        speak("Answer Now:")

        ##engine.runAndWait()
        
        print("before",i)
        ans = listener(2)
        snapshot()
        if(ans=='repeat' or ans =='e'):
            print("after",i)
            speak("Question will be repeated. Please answer carefully")
            #engine.runAndWait()
            continue
        
        speak("Is your answer option " + ans)
        #engine.runAndWait()

        confirm = listener(2)

        speak("You said " + confirm)
        #engine.runAndWait()
        if confirm.lower() == "no":
            speak("Question will be repeated. Please answer carefully")
            #engine.runAndWait()
            continue

        answers.append(ans)
        print(ans)

        if(i < 3):
            i+=1
    score=0
    
    i = false
    while(i==false):
        speak("Talk for authentication")
        # print("hereeeeee")
        record_audio_test()
        username = test_model()
        speak("Are you "+username)
        yon=listener(2)
        if(yon.lower()=='yes'):
            break
    print(c_answers,answers,score)

    for j in range(len(c_answers)):
        if(c_answers[j]==answers[j]):
            score+=1

    print(c_answers,answers,score)

    speak("You have scored a total of " + str(score) +" out of "+str(len(data)) + " questions")
    #engine.runAndWait()


mcq_for_test()