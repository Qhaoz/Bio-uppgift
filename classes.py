# klass där man ser filmer
class Movie:
    def __init__(self, titel, tid, salong, aldersgrans):
        self.titel = titel
        self.tid = tid
        self.salong = salong
        self.aldersgrans = aldersgrans

    def info(self):
        return f"{self.titel}, Tid: {self.tid}, {self.salong}, åldersgräns: {self.aldersgrans} år"


# klass där man ser biljettpris


class Biljett:
    def __init__(self, namn, pris):
        self.namn = namn
        self.pris = pris

    def info(self):
        return f"{self.namn}: {self.pris} kr"

# klass där man ser snacks/dryck


class Product:
    def __init__(self, namn, pris):
        self.namn = namn
        self.pris = pris

    def info(self):
        return f"{self.namn}: {self.pris} kr"
