import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class Chatbot:
	# def __init__(self):
	# 	pass

	def speech(self):
		engine.say(audio)
		engine.runAndWait()

	def takeCommand(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening")
			r.adjust_for_ambient_noise(source)
			r.pause_threshold = 1
			r.energy_threshold = 1150
			audio = r.listen(source)

		try:
			print("recognize...")
			query = r.recognize_google(audio, language="bn-BD")
			print(f"User : {query}\n")
		except Exception as e:
			print(e)
			print("Say Again")
			return "None"

p = Chatbot()
q = p.takeCommand()


