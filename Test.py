import grafikinterface_new
import threading
import person
from tkinter import *
from threading import Thread


if __name__ == "__main__":
    Jan = person.Person("Jan-Luca", "Nettingsmeier", "03.08.99", "057326302", "Auf der Bülte", "59", "32584", "Löhne")


    main = Tk()

    mainGUI = grafikinterface_new.mainGui(main, 2)
    mainGUI.anzahlPersonenErhöhen()
    mainGUI.personGescannt(Jan)
    mainGUI.write([Jan])

    main.mainloop()
