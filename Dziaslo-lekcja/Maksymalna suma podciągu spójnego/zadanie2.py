import random

tablica = []

for i in range(20):
    tablica.append(random.randint(-100, 100))

szukana_suma = int(input("Podaj szukaną sumę podciągu spójnego: "))
licznik = 0

for i in range(len(tablica)):
    akt_suma = 0

    for j in range(i, len(tablica)):
        akt_suma = akt_suma + tablica[j]

        if akt_suma == szukana_suma:
            licznik += 1

print("Tablica:", tablica)
print("Liczba podciągów o podanej sumie:", licznik)