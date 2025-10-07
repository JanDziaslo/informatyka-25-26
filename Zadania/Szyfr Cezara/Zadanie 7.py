alfabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

licznik = [0] * len(alfabet)

with open("dane_7.txt", "r") as dane:
    for linia in dane:
        slowa = linia.split()
        for slowo in slowa:
            pierwsza = slowo[0]
            indeks = alfabet.index(pierwsza)
            licznik[indeks] += 1

for i in range(len(alfabet)):
    if licznik[i] > 0:
        print(f"Litera: {alfabet[i]}, wystepuje na początku {licznik[i]} wyrazów")


