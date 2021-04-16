#import packages
import cv2
from pyzbar import pyzbar
import imutils
from imutils.video import VideoStream
import time
import pickle
import threading
from tkinter import *
import grafikinterface
import re
from person import Person
# get access to LEDs connected to RPi
from gpiozero import LED
# get keypad class from keypad.py
from keypad import keypad
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def inputDigit(kp):
    digit = None
    while digit == None:
        digit = kp.getKey()
    time.sleep(0.4)
    return str(digit)


def dateInput():
    kp = keypad(columnCount = 4)
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
    kp.exit()
    return day1 + day2 + dot1 + month1 + month2 + dot2 + year1 + year2 + year3 + year4


def scan(gui, date, pin):
    dateReplaced = date.replace('*', '_')
    dateFile = dateReplaced + '.p'

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

    # loop over frames
    while True:
        frame = vs.read()
        # resize image for better performance
        #frame = imutils.resize(frame, width=1000)
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            # decode data input
            decodedCode = barcode.data.decode()
            dataArray = decodedCode.replace(' ', '').split('}')
            try:
                checkString = dataArray[0]
                if checkString != "BAU":
                    print('Wrong code')
                    break
                new_person = Person(dataArray[1], dataArray[2], dataArray[3], dataArray[4],
                                    dataArray[5], dataArray[6], dataArray[7], dataArray[8])
                # check if new_person is already contained in persons list
                if any(person for person in persons if (person.__repr__() == new_person.__repr__())):
                    print('Person already registered')
                    # wait 2 seconds
                    time.sleep(2.0)
                    break
                persons.append(new_person)
                gui.write(persons)
                led.on()
                print('Wait...')
                # serialize persons list (open file in write-binary-mode)
                pickle.dump(persons, open(dateFile, 'wb'))
                print(persons)
                time.sleep(2.0)
                led.off()
                print('Scan:')
            except IndexError:
                print('Malicious QR-Code')


if __name__ == "__main__":
    #disable GPIO warnings
    #GPIO.setwarnings(False)

    # wait for input of date
    matchObject = None
    while not matchObject:
        date = dateInput()
        print(date)
        matchObject = re.match("^[0-9][0-9]\*[0-9][0-9]\*[0-9][0-9][0-9][0-9]$", date)
        if not matchObject:
            print('Falsches Datum!')

    # create gui
    global gui
    main = Tk()
    mainGUI = grafikinterface.mainGui(main)
    # start scanner thread
    try:
        scanThread = threading.Thread(
            target=scan, args=(mainGUI, date, 17), daemon=True)
        scanThread.start()
        main.mainloop()
    except KeyboardInterrupt:
        print("Leaving...")
