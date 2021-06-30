import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime
import sys
import pandas as pd
import random

listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty("voices")
engine.setProperty('voice', voice[38].id) 


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

def blague():
	numero = random.randrange(0, 103)
	blagues = pd.read_csv('./blagues/questions.csv')
	blague = blagues.iloc[numero, 0]
	reponses = pd.read_csv('./blagues/reponses.csv')
	reponse = reponses.iloc[numero,0]
	print(blague)
	parler(blague)
	parler(reponse)
	print(reponse)

	
		

def lancer_assistant():
	command = ecouter()
	print(command)
	if 'chanson de' in command: 
		artiste= command.replace('joue une chanson de', '')
		pywhatkit.playonyt(artiste, use_api=True)
		print(artiste)
		parler('je joue une chanson de  {}'.format(artiste))
	elif 'bonjour' in command:
		with sr.Microphone() as source:
			parler("Bonjour, comment vous apellez vous ? ")
			prenom=listener.listen(source)
			prenom=listener.recognize_google(prenom,language='fr-FR')
			prenom = prenom.lower()
			if prenom == "louis":
				prenom = "maitre"
			elif prenom == "claire":
				prenom = "la pesteuse"
			parler("ravi de faire votre connaissance" + prenom )
		return prenom
	elif 'éteins-toi' in command:
		parler("ok je m'éteint")
		sys.exit()
	elif 'heure' in command:
		heure = datetime.datetime.now().strftime('%H:%M')
		parler(' il est '+ heure)
	elif 'blague' in command:
		blague()
	
	else:
		parler("je ne comprend pas  ")
		print("je ne comprend pas ")

while True:
	 lancer_assistant()
	 