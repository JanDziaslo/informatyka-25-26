# Przygotuj plik tekstowy z dowolnym tekstem składającym się ze słów o długości nie większej niż 10 liter i ze
# spacji oddzielających wyrazy. Napisz program, który odczyta dane z pliku wejściowego i wypisze, ile jest w nim
# wyrazów o poszczególnych długościach (od 1 do 10)

dlugosci = "0123456789"

licznik = [0] * 10

plik = "dane_6.txt"

with open(plik, "r") as dane:
    for linia in dane:
        for slowo in linia.split():
            dlugosc = str(len(slowo))
            indeks = dlugosci.index(dlugosc)
            licznik[indeks] += 1

for i in range(len(dlugosci)):
    if licznik[i] > 0:
        print(f"Wyrazy o długości: {dlugosci[i]} wystepują {licznik[i]} razy")