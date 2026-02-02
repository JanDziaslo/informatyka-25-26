import random

tablica = []

for i in range(20):
    tablica.append(random.randint(-100, 100))

maks_suma = tablica[0]
akt_suma = tablica[0]

for i in range(1, len(tablica)):
    if akt_suma < 0:
        akt_suma = tablica[i]
    else:
        akt_suma = akt_suma + tablica[i]

    if akt_suma > maks_suma:
        maks_suma = akt_suma

print("Tablica:", tablica)
print("Maksymalna suma podciągu spójnego:", maks_suma)


