
n = int(input("Podaj liczbę elementów: "))

tab = []
print("Wprowadź tekst:")
for i in range(n):
    tab.append(input())

for i in range(n - 1):
    pmin = i

    for j in range(i + 1, n):
        if len(tab[j]) < len(tab[pmin]):
            pmin = j

    tab[i], tab[pmin] = tab[pmin], tab[i]
#opa
print("Posortowana tablica według długości:")
for slowo in tab:
    print(f"{slowo} (długość: {len(slowo)})")
