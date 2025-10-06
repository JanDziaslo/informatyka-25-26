tekst = input("Podaj tekst: ")

alfabet = "abcdefghijklmnopqrstuvwxyz"
liczniki = [0] * len(alfabet)

for znak in tekst.lower():
    if znak in alfabet:
        pozycja = alfabet.index(znak)
        liczniki[pozycja] += 1

maksimum = max(liczniki)

if maksimum > 0:
    print("Najczesciej wystepujace litery:")
    for i in range(len(alfabet)):
        if liczniki[i] == maksimum:
            print(alfabet[i])
else:
    print("Brak liter w tekscie")

