import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime
import sys


listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty("voices")
engine.setProperty('voice', voice[3].id) 


def parler(text):
	engine.say(text)
	engine.runAndWait()

def ecouter():
	with sr.Microphone() as source:
		print("parlez maintenant")
		voix=listener.listen(source)
		command=listener.recognize_google(voix,language='fr-FR')
		command.lower()
	return command


def lancer_assistant():
	command = ecouter()
	print(command)
	if 'joue une chanson de' in command: 
		artiste= command.replace('joue une chanson de', '')
		pywhatkit.playonyt(artiste, use_api=True)
		print(artiste)
		parler('je joue une chanson de  {}'.format(artiste))
	elif 'éteins-toi' in command:
		parler("je m'éteint")
		sys.exit()
	elif 'heure' in command:
		heure = datetime.datetime.now().strftime('%H:%M')
		parler(' il est '+ heure)
	else:
		parler("je ne comprend pas  ")
		print("je ne comprend pas ")

while True:
	 lancer_assistant()
	 