lista = [3, 1, 2, 1, 3, 3, 5, 2, 1]

wynik = {}
for element in lista:
    wynik[element] = wynik.get(element, 0) + 1

for elem in sorted(wynik):
    print(f'{elem}: {wynik[elem]}')
