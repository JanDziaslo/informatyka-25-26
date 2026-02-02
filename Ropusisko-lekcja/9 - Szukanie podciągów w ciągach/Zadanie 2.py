import random

tablica = []

n = int(input("Podaj długość tabeli: "))

for i in range(n):
    tablica.append(random.randint(-10, 10))

# Znajdowanie maksymalnej długości (podciąg ściśle rosnący)
maks_dl = 1
akt_dl = 1
for i in range(1, n):
    if tablica[i] >= tablica[i-1]:
        akt_dl += 1
    else:
        akt_dl = 1
    if akt_dl > maks_dl:
        maks_dl = akt_dl

# Zbieranie wszystkich podciągów o maksymalnej długości
podciagi = []
akt_dl = 1
if maks_dl == 1:
    for x in tablica:
        podciagi.append([x])
else:
    for i in range(1, n):
        if tablica[i] >= tablica[i-1]:
            akt_dl += 1
        else:
            akt_dl = 1

        if akt_dl == maks_dl:
            fragment = tablica[i - maks_dl + 1 : i + 1]
            podciagi.append(fragment)

# Wypisywanie wyników
print(f"Maksymalna długość wynosi: {maks_dl}")
print("Wszystkie najdłuższe podciągi:")
for p in podciagi:
    print(*p)

if podciagi:
    print("Ostatni znaleziony najdłuższy podciąg:")
    print(*podciagi[-1])
