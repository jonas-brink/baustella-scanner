from tkinter import *
from person import Person
import time
#Mode 2 aktiviert 2. Fenster.

class mainGui:
	def __init__(self, master, mode):
		self.Max = Person("Max", "Mustermann", "00.00.2000", "123456789", "Alleee", "120", "32584", "Löhne")
		self.pace = 1.0
		self.height = 1
		self.master = master
		self.counter = 0


		if mode==1:
			master.geometry("520x375+600+300")
		elif mode==2:
			master.geometry("1140x700+600+300")

		master.config(bg="white")
		master.title("Main Interface")
		master.resizable(True, True)

		#building frame grid
		self.frameTop = Frame(master, padx=50, pady=70, bg='orange')
		self.frameTop.grid(row=0, column=0)
		self.frameTopRight = Frame(master, padx=50, pady=50, bg='red')
		self.frameTopRight.grid(row=0, column=1)
		self.frameBot = Frame(master, padx=50, pady=50, bg='gray')
		self.frameBot.grid(row=1, column=0)
		self.frameBotRight = Frame(master, padx=50, pady=50, bg='gray')
		self.frameBotRight.grid(row=1, column=1)

		# frame for terminal
		self.frameTerminal = Frame(self.frameBot)
		self.frameTerminal.grid(row=1, column=0)
		self.frameTerminal.configure(background='black')

		# frame for terminal2
		if mode==2:
			self.frameTerminal2 = Frame(self.frameBotRight)
			self.frameTerminal2.grid(row=1, column=0)
			self.frameTerminal2.configure(background='black')

		# create scrollbar
		self.scrollbar = Scrollbar(self.frameTerminal)
		self.scrollbar.pack(side=RIGHT, fill="y")

		# create scrollbar2
		if mode==2:
			self.scrollbar2 = Scrollbar(self.frameTerminal2)
			self.scrollbar2.pack(side=RIGHT, fill="y")

		# create output
		self.output = Listbox(self.frameTerminal, yscrollcommand=self.scrollbar.set, width=50, height=15,
                              background='black', fg='white')
		self.output.pack(side=LEFT)
		self.scrollbar.config(command=self.output.yview)

		# create output2
		if mode==2:
			self.output2 = Listbox(self.frameTerminal2, yscrollcommand=self.scrollbar2.set, width=50, height=15,
                	               background='black', fg='white')
			self.output2.pack(side=LEFT)
			self.scrollbar2.config(command=self.output2.yview)


		#Labels Mode 2

		if mode==2:
			self.bausetllaLabel21 = Label(self.frameTop, text="Baustella Scanner", bg="black", fg="white", font=("Courier", 44)).grid(row=0, column=0, columnspan = 2, padx='5', pady='5', sticky='ew')
			self.bausetllaLabel211 = Label(self.frameTop, text="Bereit", bg="green", fg="white",font=("Courier", 22)).grid(row=1, column=0,columnspan = 2, padx='5', pady='5', sticky='ew')
			self.bausetllaLabel212 = Label(self.frameTop, text="Anwesend:", bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=0, padx='5', pady='5', sticky='ew')
			self.bausetllaLabel213 = Label(self.frameTop, text=str(self.counter), bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=1, padx='5', pady='5', sticky='ew')

			self.bausetllaLabel22 = Label(self.frameTopRight, text="Aktuell Erkannt:", bg="black", fg="white",font=("Courier", 16), width="45").grid(row=0, column=0, columnspan = 2, padx='5', pady='5', sticky='ew')
			self.bausetllaLabel221 = Label(self.frameTopRight, text="Name:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=1, column=0, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel222 = Label(self.frameTopRight, text="Max Mustermann", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=1, column=1, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel223 = Label(self.frameTopRight, text="Geburtsdatum:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=2, column=0, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel224 = Label(self.frameTopRight, text="01.01.2000", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=2, column=1, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel225 = Label(self.frameTopRight, text="Telefonnummer:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=3, column=0, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel226 = Label(self.frameTopRight, text="0123456789", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=3, column=1, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel227 = Label(self.frameTopRight, text="Straße & Hausnummer:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=4, column=0, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel228 = Label(self.frameTopRight, text="Alleee 120", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=4, column=1, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel229 = Label(self.frameTopRight, text="PLZ & Ort:", bg="black", fg="white",font=("Courier", 12), width="15").grid(row=5, column=0, padx='5', pady='0',sticky='ew')
			self.bausetllaLabel2210 = Label(self.frameTopRight, text="32584 Löhne", bg="black", fg="white", font=("Courier", 12),width="30").grid(row=5, column=1, padx='5', pady='0', sticky='ew')
			self.bausetllaLabel2211 = Label(self.frameTopRight, text="Uhrzeit der Erfassung:", bg="black", fg="white",font=("Courier", 12), width="15").grid(row=5, column=0, padx='5', pady='0',sticky='ew')
			self.bausetllaLabel2212 = Label(self.frameTopRight, text="00:00 Uhr", bg="black", fg="white", font=("Courier", 12),width="30").grid(row=5, column=1, padx='5', pady='0', sticky='ew')

			self.bausetllaLabel23 = Label(self.frameBot, text="Anwesende Personen", bg="black", fg="green").grid(row=0, column=0, padx='5', pady='5', sticky='ew')

			self.bausetllaLabel24 = Label(self.frameBotRight, text="Abwesende Personen", bg="black", fg="red").grid(row=0, column=0, padx='5', pady='5', sticky='ew')




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
		self.master.update()
		time.sleep(3)

		self.personAnzeigen(person)
		self.anzahlPersonenErhöhen()
		self.bausetllaLabel211 = Label(self.frameTop, text="Warten : 5", bg="red", fg="white", font=("Courier", 22)).grid(row=1, column=0, columnspan=2, padx='5', pady='5', sticky='ew')
		self.master.update()
		time.sleep(1)
		self.bausetllaLabel214 = Label(self.frameTop, text="Warten : 4", bg="red", fg="white", font=("Courier", 22)).grid(row=1, column=0, columnspan=2, padx='5', pady='5', sticky='ew')
		self.master.update()
		time.sleep(1)
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

	def personAnzeigen(self, person):
		self.bausetllaLabel222 = Label(self.frameTopRight, text=person.vorname+" "+person.nachname, bg="black", fg="white",font=("Courier", 12), width="30").grid(row=1, column=1, padx='5', pady='0',sticky='ew')
		self.bausetllaLabel224 = Label(self.frameTopRight, text=person.gebdatum, bg="black", fg="white", font=("Courier", 12), width="30").grid(row=2, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel226 = Label(self.frameTopRight, text=person.telefonnr, bg="black", fg="white", font=("Courier", 12), width="30").grid(row=3, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel228 = Label(self.frameTopRight, text=person.strasse+" "+person.hausnr, bg="black", fg="white", font=("Courier", 12), width="30").grid(row=4, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel2210 = Label(self.frameTopRight, text=person.plz+" "+person.ort, bg="black", fg="white", font=("Courier", 12), width="30").grid(row=5, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel2212 = Label(self.frameTopRight, text="00:00 Uhr", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=5, column=1, padx='5', pady='0', sticky='ew')


	#def write2(self, txt):
	#	if txt == "BLANK":
	#		self.output2.insert(END, "\n")
	#	else:
	#		self.output2.insert(END, str(txt + "\n"))
	#		self.output2.see("end")



