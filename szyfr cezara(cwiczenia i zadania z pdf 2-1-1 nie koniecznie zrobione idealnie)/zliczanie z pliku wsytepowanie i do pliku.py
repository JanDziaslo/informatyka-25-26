plik = open("zliczanie.txt", "r", encoding="utf-8")
tekst = plik.read()
plik.close()

alfabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
liczniki = [0] * len(alfabet)

for znak in tekst.lower():
    if znak in alfabet:
        pozycja = alfabet.index(znak)
        liczniki[pozycja] += 1

plik_wynik = open("wyniki.txt", "w", encoding="utf-8")
for i in range(len(alfabet)):
    if liczniki[i] > 0:
        plik_wynik.write(f"{alfabet[i]}: {liczniki[i]}\n")
plik_wynik.close()

print("Zliczono litery i zapisano do pliku wyniki.txt")
