plik = open("tajne_angielski.txt", "r", encoding="utf-8")
szyfrogram = plik.read()
plik.close()

alfabet = "abcdefghijklmnopqrstuvwxyz"
liczniki = [0] * len(alfabet)

for znak in szyfrogram.lower():
    if znak in alfabet:
        pozycja = alfabet.index(znak)
        liczniki[pozycja] += 1

maksimum = max(liczniki)
indeks_najczestszej = 0
for i in range(len(liczniki)):
    if liczniki[i] == maksimum:
        indeks_najczestszej = i
        break

indeks_e = alfabet.index('e')
klucz = (indeks_najczestszej - indeks_e) % len(alfabet)

odszyfrowany = ""
for znak in szyfrogram:
    if znak.lower() in alfabet:
        czy_wielka = znak.isupper()
        pozycja = alfabet.index(znak.lower())
        nowa_pozycja = (pozycja - klucz) % len(alfabet)
        nowy_znak = alfabet[nowa_pozycja]
        if czy_wielka:
            nowy_znak = nowy_znak.upper()
        odszyfrowany += nowy_znak
    else:
        odszyfrowany += znak

plik_wynik = open("odszyfrowane_angielski.txt", "w", encoding="utf-8")
plik_wynik.write(odszyfrowany)
plik_wynik.close()

print(f"Najczesciej wystepujaca litera w szyfrogramie: {alfabet[indeks_najczestszej]}")
print(f"Znaleziony klucz: {klucz}")
print(f"Odszyfrowany tekst zapisano do pliku odszyfrowane_angielski.txt")
print(f"\nPodglad odszyfrowanego tekstu:")
print(odszyfrowany[:200])

