# Napisz program deszyfrujący krótki tekst zakodowany szyfrem Cezara, wczytany z klawiatury. Po każdej próbie
# deszyfrowania program zapyta, czy wypisany wynik jest poprawny. Jeśli uda się odszyfrować tekst, program
# zakończy działanie, w przeciwnym przypadku – spróbuje odszyfrować kryptogram kolejnym kluczem.


alfabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

zakodowany = str(input("Podaj zakodowany tekst: "))

for i in range(1, len(alfabet)):
    odkodowany = ""
    for znak in zakodowany:
        if znak.lower() in alfabet:
            czy_wielka = znak.isupper()
            pozycja = alfabet.index(znak.lower())
            nowa_pozycja = (pozycja - i) % len(alfabet)
            nowy_znak = alfabet[nowa_pozycja]
            if czy_wielka:
                nowy_znak = nowy_znak.upper()
            odkodowany += nowy_znak
        else:
            odkodowany += znak

    print(f"\nKlucz {i}: {odkodowany}")
    odpowiedz = input("Czy to poprawny wynik? (tak/nie): ")

    if odpowiedz.lower() == "tak":
        print(f"Tekst odszyfrowany kluczem: {i}")
        break