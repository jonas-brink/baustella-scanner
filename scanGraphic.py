from tkinter import *
from person import Person
import time

class mainGui:
	def __init__(self, master, mode):
		self.noOne = Person(" ", " ", " ", " ", " ", " ", " ", " ")
		self.master = master
		self.counter = 0

		master.geometry("1280x1024")

		master.config(bg="#202020")
		master.title("Main Interface")
		master.resizable(True, True)
		master.columnconfigure(0, weight=1)
		master.columnconfigure(1, weight=1)
		master.rowconfigure(0, weight=1)
		master.rowconfigure(1, weight=1)

		#building frame grid
		self.frameTop = Frame(master, padx=30, pady=10, bg='#202020')
		self.frameTop.grid(row=0, column=0, sticky=E+W+N+S)
		self.frameTopRight = Frame(master, padx=30, pady=10, bg='#202020')
		self.frameTopRight.grid(row=1, column=0, sticky=E+W+N+S)
		self.frameBot = Frame(master, padx=30, pady=10, bg='#202020')
		self.frameBot.grid(row=0, column=1, rowspan=2, sticky=E+W+N+S)
		self.frameBotRight = Frame(master, padx=30, pady=10, bg='#202020')

		self.frameTop.rowconfigure(0, weight=1)
		self.frameTop.rowconfigure(1, weight=1)
		self.frameTop.rowconfigure(2, weight=1)
		self.frameTop.columnconfigure(0, weight=1)
		self.frameTop.columnconfigure(1, weight=1)

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
		self.frameTerminal.columnconfigure(0, weight=1)
		self.frameTerminal.grid(row=1, column=0, sticky=E+W+N+S)
		self.frameTerminal.configure(background='blue')

		# create scrollbar
		self.scrollbar = Scrollbar(self.frameTerminal)
		self.scrollbar.grid(column=1, row=0, sticky='NS')

		# create output
		self.output = Listbox(self.frameTerminal, yscrollcommand=self.scrollbar.set, width=50, height=30, background='black', fg='white', font=('Helvetica', 14))
		self.output.grid(row=0, column=0, sticky='NSEW')
		self.scrollbar.config(command=self.output.yview)
		self.output.bind("<q>", lambda event: self.output.see(0))
		self.output.bind("<w>", lambda event: self.output.yview_scroll(-1, "units"))
		self.output.bind("<s>", lambda event: self.output.yview_scroll(1, "units"))
		self.output.focus_set()

		self.bausetllaLabel21 = Label(self.frameTop, text="Baustella Scanner", bg="black", fg="white", font=("Courier", 44)).grid(row=0, column=0, columnspan = 2, padx='5', pady='5', sticky='ew')
		self.bausetllaLabel211 = Label(self.frameTop, text="Bereit", bg="green", fg="white",font=("Courier", 22)).grid(row=1, column=0,columnspan = 2, padx='5', pady='5', sticky='ew')
		self.bausetllaLabel212 = Label(self.frameTop, text="Anwesend:", bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=0, padx='5', pady='5', sticky='ew')
		self.bausetllaLabel213 = Label(self.frameTop, text=str(self.counter), bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=1, padx='5', pady='5', sticky='ew')

		self.bausetllaLabel22 = Label(self.frameTopRight, text="Aktuell Erkannt:", bg="black", fg="white",font=("Courier", 16), width="45").grid(row=0, column=0, columnspan = 2, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel221 = Label(self.frameTopRight, text="Name:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=1, column=0, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel222 = Label(self.frameTopRight, text=" ", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=1, column=1, padx='5', pady='0',sticky=E+W+N+S)
		self.bausetllaLabel223 = Label(self.frameTopRight, text="Geburtsdatum:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=2, column=0, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel224 = Label(self.frameTopRight, text=" ", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=2, column=1, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel225 = Label(self.frameTopRight, text="Telefonnummer:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=3, column=0, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel226 = Label(self.frameTopRight, text=" ", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=3, column=1, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel227 = Label(self.frameTopRight, text="Stra??e & Hausnummer:", bg="black", fg="white", font=("Courier", 12), width="15").grid(row=4, column=0, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel228 = Label(self.frameTopRight, text=" ", bg="black", fg="white", font=("Courier", 12), width="30").grid(row=4, column=1, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel229 = Label(self.frameTopRight, text="PLZ & Ort:", bg="black", fg="white",font=("Courier", 12), width="15").grid(row=5, column=0, padx='5', pady='0',sticky=E+W+N+S)
		self.bausetllaLabel2210 = Label(self.frameTopRight, text=" ", bg="black", fg="white", font=("Courier", 12),width="30").grid(row=5, column=1, padx='5', pady='0', sticky=E+W+N+S)
		self.bausetllaLabel23 = Label(self.frameBot, text="Anwesende Personen", bg="black", fg="green").grid(row=0, column=0, padx='5', pady='5', sticky='ew')


	def write(self, persons):
		self.output.delete(0, END)
		for person in persons:
			self.output.insert(END, str(person.__repr__()))
			self.output.see("end")
		self.setAnzahlPersonen(len(persons))

	def anzahlPersonenErh??hen(self):
		self.counter = self.counter +1
		self.bausetllaLabel213 = Label(self.frameTop, text=str(self.counter), bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=1, padx='5', pady='5', sticky='ew')

	def anzahlPersonenSenken(self):
		self.counter = self.counter -1
		self.bausetllaLabel213 = Label(self.frameTop, text=str(self.counter), bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=1, padx='5', pady='5', sticky='ew')

	def setAnzahlPersonen(self, anzahl):
		self.counter = anzahl
		self.bausetllaLabel213 = Label(self.frameTop, text=str(self.counter), bg="blue", fg="white", font=("Courier", 16)).grid(row=2, column=1, padx='5', pady='5', sticky='ew')

	def personGescannt(self, person):
		self.frameTopRight.config(bg='green')
		self.personAnzeigen(person)
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
		self.personAnzeigen(self.noOne)
		self.frameTopRight.config(bg='#202020')

	def personAnzeigen(self, person):
		self.bausetllaLabel222 = Label(self.frameTopRight, text=person.vorname.replace('\\', '')+" "+person.nachname.replace('\\', ''), bg="black", fg="white",font=("Courier", 12), width="30").grid(row=1, column=1, padx='5', pady='0',sticky='ew')
		self.bausetllaLabel224 = Label(self.frameTopRight, text=person.gebdatum.replace('\\', ''), bg="black", fg="white", font=("Courier", 12), width="30").grid(row=2, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel226 = Label(self.frameTopRight, text=person.telefonnr.replace('\\', ''), bg="black", fg="white", font=("Courier", 12), width="30").grid(row=3, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel228 = Label(self.frameTopRight, text=person.strasse.replace('\\', '')+" "+person.hausnr.replace('\\', ''), bg="black", fg="white", font=("Courier", 12), width="30").grid(row=4, column=1, padx='5', pady='0', sticky='ew')
		self.bausetllaLabel2210 = Label(self.frameTopRight, text=person.plz.replace('\\', '')+" "+person.ort.replace('\\', ''), bg="black", fg="white", font=("Courier", 12), width="30").grid(row=5, column=1, padx='5', pady='0', sticky='ew')