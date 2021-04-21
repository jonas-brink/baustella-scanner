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


class Person:
    def __init__(self, vorname, nachname, telefonnr, strasse, hausnr, plz, ort, email):
        self.vorname = vorname
        self.nachname = nachname
        self.telefonnr = telefonnr
        self.strasse = strasse
        self.hausnr = hausnr
        self.plz = plz
        self.ort = ort
        self.email = email

    def __repr__(self):
        return self.vorname + ' ' + self.nachname


def scan():
    # TODO: check date and create file
    global date
    dateReplaced = date.replace('.', '_')
    dateFile = dateReplaced + '.p'

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
                # get persons list from files
                try:
                    # open file in read-binary-mode
                    persons = pickle.load(open(dateFile, 'rb'))
                except FileNotFoundError:
                    # create empty list if no saved file is found
                    persons = []
                new_person = Person(dataArray[1], dataArray[2], dataArray[3], dataArray[4],
                                    dataArray[5], dataArray[6], dataArray[7], dataArray[8])
                persons.append(new_person)
                gui.write(persons)
                #print ('Wait...')
                # serialize persons list (open file in write-binary-mode)
                pickle.dump(persons, open(dateFile, 'wb'))
                print(persons)
                time.sleep(3.0)
                print('Scan:')
            except IndexError:
                print('Malicious QR-Code')


if __name__ == "__main__":
    # wait for input of date
    global date
    while True:
        inputDate = input('Date: ')
        matchObject = re.match(
            "^[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9][0-9][0-9]$", inputDate)
        if matchObject:
            print('Accepted.')
            date = matchObject.match
            print(date)
            break

    # create gui
    global gui
    main = Tk()
    gui = grafikinterface.mainGui(main)
    # start scanner thread
    try:
        scanThread = threading.Thread(target=scan, daemon=True)
        scanThread.start()
        main.mainloop()
    except KeyboardInterrupt:
        print("Leaving...")
