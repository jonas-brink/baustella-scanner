import grafikinterface
import threading
import person
from tkinter import *


if __name__ == "__main__":
    #Jan = person("Jan-Luca", "Nettingsmeier", "03.08.99", "057326302", "Auf der Bülte", "59", "32584", "Löhne")
    main = Tk()
    mainGUI = grafikinterface.mainGui(main, 2)
    mainGUI.anzahlPersonenSenken()

    main.mainloop()


