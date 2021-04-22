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
