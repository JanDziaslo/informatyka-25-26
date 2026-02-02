n = int(input("Podaj liczbę elementów: "))

tab = []
print("Wprowadź elementy:")
for i in range(n):
    tab.append(int(input()))

for i in range(n - 1):
    pmin = i

    for j in range(i + 1, n):
        if tab[j] < tab[pmin]:
            pmin = j

    tab[i], tab[pmin] = tab[pmin], tab[i]

print("Posortowana tablica:")
print(tab)
