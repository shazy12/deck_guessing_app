import speech_recognition as sr
import sys

def prompt_response():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		
	try:
		return r.recognize_google(audio, language='en-IN')
	except(sr.UnknownValueError):
		print("IBM Speech Recognition could not understand audio")
		return 'Un-recognized Speech'

