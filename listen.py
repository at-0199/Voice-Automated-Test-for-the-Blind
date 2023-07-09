import speech_recognition as sr  
import time

r = sr.Recognizer()

def listener(time_lim):
    try:
        with sr.Microphone() as source:
            print("Speak:")
            aud = r.listen(source,phrase_time_limit=time_lim)  #set to 10 for subjective test

        response = r.recognize_google(aud)

    except:
        response = "Didn't catch that"

    return (response)


# a = listener()

# print(a)

