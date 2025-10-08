wejscie = "szyfrogram_Vigenere.txt"

klucz_dl = int(input("Podaj dlugosc klucza: "))

while klucz_dl > 5 and klucz_dl < 0:
    klucz_dl = int(input("Podaj dlugosc klucza: "))

klucz = "VIGENERE"[:klucz_dl]
deszyfr = ""
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open(wejscie, "r") as dane:
    for linia in dane:
        for znak in linia:
            if znak.upper() in alfabet:
                pozycja = alfabet.index(znak.upper())
                nowa_pozycja = (pozycja - klucz.index(znak)) % len(alfabet)
                nowy_znak = alfabet[nowa_pozycja]
                if znak.isupper():
                    print(nowy_znak.upper(), end="")
                else:
                    print(nowy_znak, end="")
            deszyfr += nowy_znak

print(deszyfr)