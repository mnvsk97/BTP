from gtts import gTTS
import csv
import os

with open('sample.csv', 'rb') as f:
	ifile  = open('sample.csv', "r")
	read = csv.reader(ifile)
	for row in read:
		text=''.join(map(str, row))
		language = 'en'
		myobj = gTTS(text=text, lang=language, slow=False)
		myobj.save("sample.mp3")
		os.system("mpg321 sample.mp3")

