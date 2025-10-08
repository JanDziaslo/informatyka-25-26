szyfrogram = input("Podaj zaszyfrowany tekst: ")

alfabet = "abcdefghijklmnopqrstuvwxyz"

for klucz in range(len(alfabet)):
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

    print(f"\nKlucz {klucz}: {odszyfrowany}")
    odpowiedz = input("Czy to poprawny wynik? (tak/nie): ")

    if odpowiedz.lower() == "tak":
        print(f"Tekst odszyfrowany kluczem: {klucz}")
        break
