import pyttsx3 as ttx

engine = ttx.init()
voice = engine.getProperty("voices")

for y in range(30):
	voice = engine.getProperty("voices")
	engine.setProperty('voice', voice[y].id) 
	engine.say('bonjour comment ça va ')
	print('voie n°',y)
	engine.runAndWait()

