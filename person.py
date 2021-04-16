class Person:
    def __init__(self, vorname, nachname, gebdatum, telefonnr, strasse, hausnr, plz, ort):
        self.vorname = vorname
        self.nachname = nachname
        self.gebdatum = gebdatum
        self.telefonnr = telefonnr
        self.strasse = strasse
        self.hausnr = hausnr
        self.plz = plz
        self.ort = ort

    def __repr__(self):
        return self.vorname + ' ' + self.nachname
