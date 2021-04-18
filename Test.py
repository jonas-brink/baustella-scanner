import grafikinterface
from tkinter import *

if __name__ == "__main__":
    main = Tk()
    gui = grafikinterface.mainGui(main)
    gui.write("test")
    gui.write2("test2")
    main.mainloop()




