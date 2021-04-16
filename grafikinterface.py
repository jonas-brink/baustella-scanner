from tkinter import *
class mainGui:
    def __init__(self, master):
        self.pace = 1.0
        self.height = 1
        self.master = master
        master.geometry("1500x700")
        master.config(bg="white")
        master.title("Main Interface")
        master.resizable(True, True)

        #building frame grid
        self.frameTop = Frame(master, padx=50, pady=50)
        self.frameTop.grid(row=0, column=0)
        self.frameTopRight = Frame(master, padx=50, pady=50)
        self.frameTopRight.grid(row=0, column=1)
        self.frameBot = Frame(master, padx=50, pady=50)
        self.frameBot.grid(row=1, column=0)
        self.frameBotRight = Frame(master, padx=50, pady=50)
        self.frameBotRight.grid(row=1, column=1)

        # frame for terminal
        self.frameTerminal = Frame(self.frameBotRight)
        self.frameTerminal.grid(row=2, column=3)
        self.frameTerminal.configure(background='black')

        # frame for terminal2
        self.frameTerminal2 = Frame(self.frameBot)
        self.frameTerminal2.grid(row=0, column=0)
        self.frameTerminal2.configure(background='black')

        # create scrollbar
        self.scrollbar = Scrollbar(self.frameTerminal)
        self.scrollbar.pack(side=RIGHT, fill="y")

        # create scrollbar2
        self.scrollbar2 = Scrollbar(self.frameTerminal2)
        self.scrollbar2.pack(side=RIGHT, fill="y")

        # create output
        self.output = Listbox(self.frameTerminal, yscrollcommand=self.scrollbar.set, width=50, height=15,
                              background='black', fg='white')
        self.output.pack(side=LEFT)
        self.scrollbar.config(command=self.output.yview)

        # create output
        self.output2 = Listbox(self.frameTerminal2, yscrollcommand=self.scrollbar2.set, width=50, height=15,
                               background='black', fg='white')
        self.output2.pack(side=LEFT)
        self.scrollbar2.config(command=self.output2.yview)

    def write(self, persons):
        #if txt == "BLANK":
        #    self.output.insert(END, "\n")
        #else:
        #    self.output.insert(END, str(txt + "\n"))
        #    self.output.see("end")
	for person in persons:
		self.output.insert(END, str(person.__repr__ + "\n"))
		self.output.see("end")

    def write2(self, txt):
        if txt == "BLANK":
            self.output2.insert(END, "\n")
        else:
            self.output2.insert(END, str(txt + "\n"))
        self.output2.see("end")


