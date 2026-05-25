def funkcja_hash(nazwisko):
    suma = 0
    for znak in nazwisko:
        suma += ord(znak)
    return suma % 100


class KsiazkaTelefoniczna:
    def __init__(self, rozmiar=100):
        self.rozmiar = rozmiar
        self.tablica = [[] for _ in range(rozmiar)]

    def dodaj(self, nazwisko, numer):
        indeks = funkcja_hash(nazwisko)
        for i, (nazw, tel) in enumerate(self.tablica[indeks]):
            if nazw == nazwisko:
                self.tablica[indeks][i] = (nazwisko, numer)
                return
        self.tablica[indeks].append((nazwisko, numer))

    def znajdz(self, nazwisko):
        indeks = funkcja_hash(nazwisko)
        for nazw, tel in self.tablica[indeks]:
            if nazw == nazwisko:
                return tel
        return None


ksiazka = KsiazkaTelefoniczna()

while True:
    try:
        wejscie = input()
        if not wejscie:
            break
        czesci = wejscie.split()
        if czesci[0] == "d":
            nazwisko = czesci[1]
            numer = czesci[2]
            ksiazka.dodaj(nazwisko, numer)

        elif czesci[0] == "w":
            nazwisko = czesci[1]
            wynik = ksiazka.znajdz(nazwisko)
            if wynik:
                print(wynik)
            else:
                print("Nie znaleziono")
    except (EOFError, IndexError):
        break
