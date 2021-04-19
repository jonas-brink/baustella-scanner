import grafikinterface
import threading
from tkinter import *

def thread_function():
    main = Tk()
    gui = grafikinterface.mainGui(main)
    gui.write("test")
    gui.write2("test2")
    main.mainloop()

if __name__ == "__main__":
    x = threading.Thread(target=thread_function())
    x.start()



