#import packages
import cv2
from pyzbar import pyzbar
import imutils
from imutils.video import VideoStream
import time
import pickle

class Person:
	def __init__(self, vorname, nachname, telefonnr):
		self.vorname = vorname
		self.nachname = nachname
		self.telefonnr = telefonnr
	def __repr__(self):
		return self.vorname
	def get(self):
		return self.vorname + ';' + self.nachname + ';' + self.telefonnr

#initialize video stream and wait
vs = VideoStream( usePiCamera = True ).start()
time.sleep(2.0)
print ('Start...')

#loop over frames
try:
	while True:
		frame = vs.read()
		#resize image for better performance
		#frame = imutils.resize(frame, width=1000)
		barcodes = pyzbar.decode(frame)
		for barcode in barcodes:
			#decode data input
			decodedCode = barcode.data.decode()
			dataArray = decodedCode.replace(' ', '').split('}')
			date = dataArray[0]
			dateReplaced = date.replace('.', '_')
			dateFile = dateReplaced + '.p'
			#get persons list from files
			try:
				#open file in read-binary-mode
				persons = pickle.load( open( dateFile, 'rb' ) )
			except FileNotFoundError:
				#create empty list if no saved file is found
				persons = []
			new_person = Person(dataArray[1], dataArray[2], dataArray[3])
			persons.append(new_person)
			#print(persons)
			print ('Wait...')
			#serialize persons list (open file in write-binary-mode)
			pickle.dump( persons, open( dateFile, 'wb' ) )
			print (persons)
			time.sleep(3.0)
			print ('GO:')
except KeyboardInterrupt:
	print ('Leaving...')
