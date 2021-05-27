class Person:
    def __init__(self, vorname, nachname, gebdatum, email, strasse, hausnr, plz, ort):
        self.vorname = vorname
        self.nachname = nachname
        self.gebdatum = gebdatum
        self.email = email
        self.strasse = strasse
        self.hausnr = hausnr
        self.plz = plz
        self.ort = ort

    def __repr__(self):
        return self.vorname + ' ' + self.nachname
