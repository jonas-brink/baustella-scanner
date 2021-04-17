from tkinter import *


class startGui:
	def __init__(self, master):
		self.master = master

		master.geometry("1280x1024")
		master.config(bg="white")
		master.title("Info")
		master.resizable(False, False)

		self.frameTop1 = Frame(master, padx=50, pady=50)
		self.frameTop1.grid(row=0, column=0)

		self.infoLabel1 = Label(self.frameTop1, text="Info", bg='#202020', fg="white", font=("Courier", 22)).grid(row=0, column=0, padx='5', pady='5', sticky='ew')

	def auswahlTreffen(self):
		self.infoLabel1 = Label(self.frameTop1, text="Wähle Modus (A: Scannen, D: Drucken): ", bg='#202020', fg="white", font=("Courier", 22)).grid(row=0, column=0, padx='5', pady='5', sticky='ew')

	def datumEingeben(self):
		self.infoLabel1 = Label(self.frameTop1, text="Bitte das Datum eingeben (TT*MM*JJJJ): ", bg='#202020', fg="white", font=("Courier", 22)).grid(row=0, column=0, padx='5', pady='5', sticky='ew')

	def uhrzeitEingeben(self):
		self.infoLabel1 = Label(self.frameTop1, text="Bitte die Uhrzeit eingeben (HH*MM): ", bg='#202020', fg="white", font=("Courier", 22)).grid(row=0, column=0, padx='5', pady='5', sticky='ew')

