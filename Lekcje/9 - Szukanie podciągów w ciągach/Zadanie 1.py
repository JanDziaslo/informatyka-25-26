tablica = []

n = int(input("Podaj długość tabeli: "))

for i in range(n):
    print(f"Podaj element {i+1} tablicy: ", end="")
    tablica.append(int(input()))

# Najdłuższe podciągi niemalejące (>=)
maks_dl = 1
akt_dl = 1
for i in range(1, n):
    if tablica[i] >= tablica[i-1]:
        akt_dl += 1
        if akt_dl > maks_dl:
            maks_dl = akt_dl
    else:
        akt_dl = 1

akt_dl = 1
if maks_dl == 1:
    for x in tablica:
        print(x)
else:
    for i in range(1, n):
        if tablica[i] >= tablica[i-1]:
            akt_dl += 1
        else:
            akt_dl = 1
        if akt_dl == maks_dl:
            for j in range(i - maks_dl + 1, i + 1):
                print(tablica[j], end=" ")
            print()

print(f"Maksymalna długość wynosi: {maks_dl}")
