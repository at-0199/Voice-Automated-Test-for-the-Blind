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
from questions import *
from Summary import *

warnings.filterwarnings("ignore")

r = sr.Recognizer()                                                                                   
 

def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)



#Starting here
speak("Hello Student! Are you ready?")
	

response = listener(2)
print("response recieved")

if "yes" in response:
	print(response)
	
	i=false
	while(i==false):

		speak("Talk for authentication")
		
		record_audio_test()
		username=test_model()
		speak("Are you "+username)
		yon=listener(2)
		if 'yes' in yon.lower():
			i=true
			break

		else :
			speak("Repeating authentication")



			
	speak("Test starts now")
	mcq_for_test()



else:
	speak("Okay, run this application when you are ready")


