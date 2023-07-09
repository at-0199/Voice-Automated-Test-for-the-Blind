from logging.config import listen
import os
import wave
import pickle
import pyaudio
import warnings
import numpy as np
from sklearn import preprocessing
from scipy.io.wavfile import read
import python_speech_features as mfcc
from sklearn.mixture import GaussianMixture
from sqlalchemy import false, true 
from listen import *
from time import time
import speech_recognition as sr  
import playsound
from gtts import gTTS
from test import *
from train import *
from Summary import *
from Answer_subject_check import *
import requests



r = sr.Recognizer()                                                                                   
 

def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)




#Starting here
speak("What is electricity?")

ans = listener(8)
if(ans):
    print("Text is " + ans)
    # url = "http://bark.phon.ioc.ee/punctuator"
    # payload = {"text":ans}
    # res = requests.post(url, data=payload)

    # print("Punctuated text is " + res.text)
    # summary = text_summary(res.text)
    summary = text_summary(ans)

if(summary):
    answer = summary

else:
    answer = ans


Marks = subj_ans(ans)

print(ans)


