from tkinter import *
from person import Person
import time
#Mode 2 aktiviert 2. Fenster.

class mainGui:
	def __init__(self, master, mode):
		self.Max = Person("Max", "Mustermann", "00.00.2000", "123456789", "Alleee", "120", "32584", "Löhne")
		self.master = master
		self.counter = 0

		if mode==1:
			master.geometry("520x375+600+300")
		elif mode==2:
			master.geometry("1280x1024")

		master.config(bg="gray")
		master.title("Main Interface")
		master.resizable(True, True)
		master.columnconfigure(0, weight=1)
		master.columnconfigure(1, weight=1)
		master.rowconfigure(0, weight=1)
		master.rowconfigure(1, weight=1)

		#building frame grid
		self.frameTop = Frame(master, padx=30, pady=10, bg='orange')
		self.frameTop.grid(row=0, column=0, sticky=E+W+N+S)
		self.frameTopRight = Frame(master, padx=30, pady=10, bg='red')
		self.frameTopRight.grid(row=1, column=0, sticky=E+W+N+S)
		self.frameBot = Frame(master, padx=30, pady=10, bg='gray')
		self.frameBot.grid(row=0, column=1, rowspan=2, sticky=E+W+N+S)
		self.frameBotRight = Frame(master, padx=30, pady=10, bg='gray')
		#self.frameBotRight.grid(row=1, column=1, sticky=E+W+N+S)

		#self.frameTop.rowconfigure(0, weight=1)
		self.frameTop.columnconfigure(0, weight=1)
		self.frameTop.columnconfigure(1, weight=1)
		self.frameTop.columnconfigure(2, weight=1)
		self.frameTop.columnconfigure(3, weight=1)

		self.frameTopRight.rowconfigure(0, weight=1)
		self.frameTopRight.rowconfigure(1, weight=1)
		self.frameTopRight.rowconfigure(2, weight=1)
		self.frameTopRight.rowconfigure(3, weight=1)
		self.frameTopRight.rowconfigure(4, weight=1)
		self.frameTopRight.rowconfigure(5, weight=1)
		self.frameTopRight.columnconfigure(0, weight=1)
		self.frameTopRight.columnconfigure(1, weight=1)
		self.frameTopRight.columnconfigure(2, weight=1)
		self.frameTopRight.columnconfigure(3, weight=1)

		self.frameBot.rowconfigure(1, weight=1)
		self.frameBot.columnconfigure(0, weight=1)
		self.frameBot.columnconfigure(1, weight=1)
		self.frameBot.columnconfigure(2, weight=1)
		self.frameBot.columnconfigure(3, weight=1)

		#self.frameBotRight.rowconfigure(0, weight=1)
		self.frameBotRight.columnconfigure(0, weight=1)
		self.frameBotRight.columnconfigure(1, weight=1)
		self.frameBotRight.columnconfigure(2, weight=1)
		self.frameBotRight.columnconfigure(3, weight=1)

		# frame for terminal
		self.frameTerminal = Frame(self.frameBot)
		self.frameTerminal.rowconfigure(0, weight=1)
		self.frameTerminal.rowconfigure(1, weight=1)
		self.frameTerminal.columnconfigure(0, weight=1)
		self.frameTerminal.columnconfigure(0, weight=1)
		self.frameTerminal.grid(row=1, sticky=E+W+N+S)
		self.frameTerminal.configure(background='black')

		# frame for terminal2
		#if mode==2:
		#	self.frameTerminal2 = Frame(self.frameBotRight)
		#	self.frameTerminal2.grid(row=1, column=0)
		#	self.frameTerminal2.configure(background='black')

		# create scrollbar
		self.scrollbar = Scrollbar(self.frameTerminal)
		self.scrollbar.grid(column=1, row=0, sticky='NS')

		# create scrollbar2
		#if mode==2:
		#	self.scrollbar2 = Scrollbar(self.frameTerminal2)
		#	self.scrollbar2.pack(side=RIGHT, fill="y")

		# create output
		self.output = Listbox(self.frameTerminal, yscrollcommand=self.scrollbar.set, width=50, height=30,
                              background='black', fg='white')
		self.output.grid(row=0, column=0, sticky=E+W+N+S)
		self.scrollbar.config(command=self.output.yview)

		# create output2
		#if mode==2:
		#	self.output2 = Listbox(self.frameTerminal2, yscrollcommand=self.scrollbar2.set, width=50, height=30,
        #        	               background='black', fg='white')
		#	self.output2.pack(side=LEFT)
		#	self.scrollbar2.config(command=self.output2.yview)


		#Labels Mode 2

		if mode==2:
			self.bausetllaLabel21 = Label(self.frameTop, text="Baustella Scanner", bg="black", fg="white", font=("Courier", 44)).grid(row=0, column=0, columnspan = 2, padx='5', pady='5', sticky='ew')
			self.bausetllaLabel211 = Label(self.frameTop, text="Bereit", bg="green", fg="white",font=("Courier", 22)).grid(row=1, column=0,columnspan = 2, padx='5', pady='5', sticky='ew')
			self.bausetllaLabel212 = Label(self.frameTop, text="Anwesend:", bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=0, padx='5', pady='5', sticky='ew')
			self.bausetllaLabel213 = Label(self.frameTop, text=str(self.counter), bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=1, padx='5', pady='5', sticky='ew')

			self.bausetllaLabel22 = Label(self.frameTopRight, text="Aktuell Erkannt:", bg="black", fg="white",font=("Courier", 16), width="45").grid(row=0, column=0, columnspan = 2, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel221 = Label(self.frameTopRight, text="Name:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=1, column=0, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel222 = Label(self.frameTopRight, text="Max Mustermann", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=1, column=1, padx='5', pady='0',sticky=E+W+N+S)
			self.bausetllaLabel223 = Label(self.frameTopRight, text="Geburtsdatum:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=2, column=0, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel224 = Label(self.frameTopRight, text="01.01.2000", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=2, column=1, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel225 = Label(self.frameTopRight, text="Telefonnummer:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=3, column=0, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel226 = Label(self.frameTopRight, text="0123456789", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=3, column=1, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel227 = Label(self.frameTopRight, text="Straße & Hausnummer:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=4, column=0, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel228 = Label(self.frameTopRight, text="Alleee 120", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=4, column=1, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel229 = Label(self.frameTopRight, text="PLZ & Ort:", bg="black", fg="white",font=("Courier", 12), width="15").grid(row=5, column=0, padx='5', pady='0',sticky=E+W+N+S)
			self.bausetllaLabel2210 = Label(self.frameTopRight, text="32584 Löhne", bg="black", fg="white", font=("Courier", 12),width="30").grid(row=5, column=1, padx='5', pady='0', sticky=E+W+N+S)
			self.bausetllaLabel2211 = Label(self.frameTopRight, text="Uhrzeit der Erfassung:", bg="black", fg="white",font=("Courier", 12), width="15").grid(row=5, column=0, padx='5', pady='0',sticky=E+W+N+S)
			self.bausetllaLabel2212 = Label(self.frameTopRight, text="00:00 Uhr", bg="black", fg="white", font=("Courier", 12),width="30").grid(row=5, column=1, padx='5', pady='0', sticky=E+W+N+S)

			self.bausetllaLabel23 = Label(self.frameBot, text="Anwesende Personen", bg="black", fg="green").grid(row=0, column=0, padx='5', pady='5', sticky='ew')

			#self.bausetllaLabel24 = Label(self.frameBotRight, text="Abwesende Personen", bg="black", fg="red").grid(row=0, column=0, padx='5', pady='5', sticky='ew')




	def write(self, persons):
		#if txt == "BLANK":
		#    self.output.insert(END, "\n")
		#else:
		#    self.output.insert(END, str(txt + "\n"))
		#    self.output.see("end")
		self.output.delete(0, END)
		for person in persons:
			self.output.insert(END, str(person.__repr__()))
			self.output.see("end")

	def anzahlPersonenErhöhen(self):
		self.counter = self.counter +1
		self.bausetllaLabel213 = Label(self.frameTop, text=str(self.counter), bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=1, padx='5', pady='5', sticky='ew')

	def anzahlPersonenSenken(self):
		self.counter = self.counter -1
		self.bausetllaLabel213 = Label(self.frameTop, text=str(self.counter), bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=1, padx='5', pady='5', sticky='ew')

	def personGescannt(self, person):
		self.frameTopRight.config(bg='green')
		self.personAnzeigen(person)
		self.anzahlPersonenErhöhen()
		#self.bausetllaLabel211 = Label(self.frameTop, text="Warten : 5", bg="red", fg="white", font=("Courier", 22)).grid(row=1, column=0, columnspan=2, padx='5', pady='5', sticky='ew')
		#self.master.update()
		#time.sleep(1)
		#self.bausetllaLabel214 = Label(self.frameTop, text="Warten : 4", bg="red", fg="white", font=("Courier", 22)).grid(row=1, column=0, columnspan=2, padx='5', pady='5', sticky='ew')
		#self.master.update()
		#time.sleep(1)
		self.bausetllaLabel214 = Label(self.frameTop, text="Warten : 3", bg="red", fg="white", font=("Courier", 22)).grid(row=1, column=0, columnspan=2, padx='5', pady='5', sticky='ew')
		self.master.update()
		time.sleep(1)
		self.bausetllaLabel214 = Label(self.frameTop, text="Warten : 2", bg="red", fg="white", font=("Courier", 22)).grid(row=1, column=0, columnspan=2, padx='5', pady='5', sticky='ew')
		self.master.update()
		time.sleep(1)
		self.bausetllaLabel214 = Label(self.frameTop, text="Warten : 1", bg="red", fg="white", font=("Courier", 22)).grid(row=1, column=0, columnspan=2, padx='5', pady='5', sticky='ew')
		self.master.update()
		time.sleep(1)
		self.bausetllaLabel211 = Label(self.frameTop, text="Bereit", bg="green", fg="white", font=("Courier", 22)).grid(row=1, column=0, columnspan=2, padx='5', pady='5', sticky='ew')
		self.master.update()
		self.personAnzeigen(self.Max)
		self.frameTopRight.config(bg='red')

	def personAnzeigen(self, person):
		self.bausetllaLabel222 = Label(self.frameTopRight, text=person.vorname.replace('\\', '')+" "+person.nachname.replace('\\', ''), bg="black", fg="white",font=("Courier", 12), width="30").grid(row=1, column=1, padx='5', pady='0',sticky='ew')
		self.bausetllaLabel224 = Label(self.frameTopRight, text=person.gebdatum.replace('\\', ''), bg="black", fg="white", font=("Courier", 12), width="30").grid(row=2, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel226 = Label(self.frameTopRight, text=person.telefonnr.replace('\\', ''), bg="black", fg="white", font=("Courier", 12), width="30").grid(row=3, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel228 = Label(self.frameTopRight, text=person.strasse.replace('\\', '')+" "+person.hausnr.replace('\\', ''), bg="black", fg="white", font=("Courier", 12), width="30").grid(row=4, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel2210 = Label(self.frameTopRight, text=person.plz.replace('\\', '')+" "+person.ort.replace('\\', ''), bg="black", fg="white", font=("Courier", 12), width="30").grid(row=5, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel2212 = Label(self.frameTopRight, text="00:00 Uhr", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=5, column=1, padx='5', pady='0', sticky='ew')


	#def write2(self, txt):
	#	if txt == "BLANK":
	#		self.output2.insert(END, "\n")
	#	else:
	#		self.output2.insert(END, str(txt + "\n"))
	#		self.output2.see("end")



