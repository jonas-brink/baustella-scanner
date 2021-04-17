import re

class Person:
    def __init__(self, vorname, nachname, gebdatum, telefonnr, strasse, hausnr, plz, ort):
        self.vorname = re.escape(vorname)
        self.nachname = re.escape(nachname)
        self.gebdatum = re.escape(gebdatum)
        self.telefonnr = re.escape(telefonnr)
        self.strasse = re.escape(strasse)
        self.hausnr = re.escape(hausnr)
        self.plz = re.escape(plz)
        self.ort = re.escape(ort)

    def __repr__(self):
        return self.vorname + ' ' + self.nachname

    def esc(self, val):
        return val.replace('\\', '')

    def getList(self):
        return [self.esc(self.vorname), self.esc(self.nachname), self.esc(self.gebdatum), self.esc(self.telefonnr), self.esc(self.strasse), self.esc(self.hausnr), self.esc(self.plz), self.esc(self.ort)]
        #print(self.ort)
        #return [self.ort.encode().decode(), '', '', '', '', '', '', '']
