#export LC_ALL=de_DE.UTF-8
# import packages
from pyzbar import pyzbar
import imutils
from imutils.video import VideoStream
import time
import pickle
import threading
from tkinter import *
import scanGraphic
import re
from person import Person
# get access to LEDs connected to RPi
from gpiozero import LED
# get keypad class from keypad.py
import keypad as Keypad
import RPi.GPIO as GPIO
from tabulate import tabulate
import pdfkit
import indexGraphic
from urllib.parse import unquote


ROWS = 4
COLS = 4
keys = ['1', '2', '3', 'A',
        '4', '5', '6', 'B',
        '7', '8', '9', 'C',
        '*', '0', '#', 'D']
# save pins of keypad occupancy
rowsPins = [7, 8, 11, 25]
colsPins = [9, 10, 15, 18]


# read digit input from keypad
def inputDigit(kp):
    digit = None
    # wait for keypress on keypad
    while digit == None or digit == kp.NULL:
        digit = kp.getKey()
    return str(digit)


# returns given date input as string
def dateInput(kp, startGui, start):
    # show label for date input
    startGui.datumEingeben()
    start.update()
    print("Bitte das Datum eingeben (TT*MM*JJJJ): ")
    # input of day
    day1 = inputDigit(kp)
    day2 = inputDigit(kp)
    # dot 1
    dot1 = inputDigit(kp)
    # input of month
    month1 = inputDigit(kp)
    month2 = inputDigit(kp)
    # dot 2
    dot2 = inputDigit(kp)
    # input of year
    year1 = inputDigit(kp)
    year2 = inputDigit(kp)
    year3 = inputDigit(kp)
    year4 = inputDigit(kp)
    return day1 + day2 + dot1 + month1 + month2 + dot2 + year1 + year2 + year3 + year4


# start scanning for QR codes in camera range
def scan(gui, dateFile, pin):
    # get persons list from files
    try:
        # open file in read-binary-mode
        persons = pickle.load(open(dateFile, 'rb'))
    except FileNotFoundError:
        # create empty list if no saved file is found
        persons = []
    gui.write(persons)

    # initialize LED
    led = LED(pin)

    # initialize video stream and wait
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    print('Start...')

    # loop over all frames
    while True:
        frame = vs.read()
        # read QR codes in frame
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            # decode data input
            decodedCode = unquote(barcode.data.decode())
            print("decoded:")
            print(decodedCode)
            # split input data on '}' (according to protocol)
            dataArray = decodedCode.split('}')
            try:
                checkString = dataArray[0]
                # check if checksum is equal to 'BAU' (according to protocol)
                if checkString != "BAU":
                    print('Wrong code')
                    break
                # create a new person with given data
                new_person = Person(dataArray[1], dataArray[2], dataArray[3], dataArray[4],
                                    dataArray[5], dataArray[6], dataArray[7], dataArray[8])
                # check if new_person is already contained in persons list
                if any(person for person in persons if (person.__repr__() == new_person.__repr__())):
                    print('Person already registered')
                    # wait 2 seconds
                    time.sleep(2.0)
                    break
                # add new person to persons list
                persons.append(new_person)
                # activate led to indicate a new record
                led.on()
                gui.write(persons)
                gui.personGescannt(new_person)
                # serialize persons list (open file in write-binary-mode)
                pickle.dump(persons, open(dateFile, 'wb'))
                # deactive led
                led.off()
            except IndexError:
                # no valid QR code found
                print('Malicious QR-Code')


if __name__ == "__main__":
    start = Tk()
    startGui = indexGraphic.startGui(start)
    # show label for choosing mode for the scanner
    startGui.auswahlTreffen()
    start.update()

    # wait for input of mode (A: scan / D: print)
    kp = Keypad.Keypad(keys, rowsPins, colsPins, ROWS, COLS)
    kp.setDebounceTime(50)
    mode = None
    while mode != 'A' and mode != 'D':
        print('Wähle Modus (A: Scannen, D: Drucken): ')
        mode = inputDigit(kp)
    print('Mode: ' + mode)

    # wait for input of date
    matchObject = None
    while not matchObject:
        date = dateInput(kp, startGui, start)
        matchObject = re.match(
            "^[0-9][0-9]\*[0-9][0-9]\*[0-9][0-9][0-9][0-9]$", date)
        if not matchObject:
            print('Falsches Datum!')
    # generate file name for input date
    dateReplaced = date.replace('*', '_')
    dateFile = dateReplaced + '.p'

    if mode == 'A':
        # activated scan mode
        try:
            # close input window
            start.destroy()
            # create gui
            global gui
            main = Tk()
            mainGUI = scanGraphic.mainGui(main, 2)
            # start scanner thread until a KeyboardInterrupt appears
            try:
                scanThread = threading.Thread(
                    target=scan, args=(mainGUI, dateFile, 17), daemon=True)
                scanThread.start()
                main.mainloop()
            except KeyboardInterrupt:
                print("Leaving...")
        finally:
            GPIO.cleanup([7, 8, 9, 10, 11, 15, 18, 25])
    elif mode == 'D':
        # activated print mode
        # load serialized persons list
        persons = pickle.load(open(dateFile, 'rb'))
        table = []
        for person in persons:
            table.append(person.getList())
        headers = ["Vorname", "Nachname", "GebDatum",
                   "TelefonNr", "Straße", "HausNr", "PLZ", "Ort"]
        # create html file from serialized data
        tableHTML = tabulate(table, headers, tablefmt="html")
        # head
        head = "<head><meta charset='utf-8'/></head>"
        tableHTML = head + tableHTML
        # css rules for html table
        css = "<style>table {border-spacing: 15px 10px;border-collapse: separate;}th {font-size: 20px;line-height: 1.5;}tr {background-color: antiquewhite;}</style>"
        tableHTML = tableHTML + css
        # write table to pdf
        pdfkit.from_string(tableHTML, dateReplaced + '.pdf')
