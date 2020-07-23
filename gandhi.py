import pyttsx3 ##using text to speech

import speech_recognition as sr ##using speech to text

from PIL import Image ##using show the image

from pydub import AudioSegment ##using audio
from pydub.playback import play

engine=pyttsx3.init()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def takecommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("listening : ")
		audio=r.listen(source)

		try:
			n=r.recognize_google(audio)

		except:
			print("say again")
			return 'none'
		return n

while True:

	n=takecommand().lower()

	if 'your name' in n:
		img=Image.open('chetan.jpg')
		img.show()
		speak(" CHETAN CHAUHAN ")

	elif '2 october' in n:
		song=AudioSegment.from_mp3('2 october.mp3')
		play(song)

	elif 'kiska bapu' in n:
		song=AudioSegment.from_mp3('bapu kon.mp3')
		play(song)

	elif 'mahatma gandhi' in n:
		song=AudioSegment.from_mp3('vo note wala.mp3')
		play(song)

	elif 'anything' in n:
		song=AudioSegment.from_mp3('or kya pta hai.mp3')
		play(song)

	elif 'in army' in n:
		song=AudioSegment.from_mp3('army gandhi.mp3')
		play(song)

		img=Image.open('gandhi1.jpeg')
		img.show()


	elif 'aapka naam' in n:
		img=Image.open('gandhi.jpg')
		img.show()
		song=AudioSegment.from_mp3('pura naam.mp3')
		play(song)

	elif 'pura naam' in n:
		song=AudioSegment.from_mp3('aapka naam.mp3')
		play(song)

	elif 'aapke pitaji ka naam' in n:
		song=AudioSegment.from_mp3('father name.mp3')
		play(song)

	elif 'mata ka naam' in n:
		song=AudioSegment.from_mp3('maa ka naam.mp3')
		play(song)

	elif 'name' in n:
		song=AudioSegment.from_mp3('hm aapko kya bulaye.mp3')
		play(song)

	

	elif 'mahatma' in n:
		song=AudioSegment.from_mp3('mahatma ka khitab.mp3')
		play(song)

	elif 'agar koi mare to' in n:
		song=AudioSegment.from_mp3('aagr koi mare.mp3')
		play(song)

	elif 'how' in n:
		song=AudioSegment.from_mp3('aagr jarrurat pade to.mp3')
		play(song)

	elif  'koi sandesh' in n:
		song=AudioSegment.from_mp3('motivational.mp3')
		play(song)
		img=Image.open('gandhi2.jpeg')
		img.show()
		song=AudioSegment.from_mp3('bande mai dum.mp3')
		play(song)


	else:
		speak('sorry')








 