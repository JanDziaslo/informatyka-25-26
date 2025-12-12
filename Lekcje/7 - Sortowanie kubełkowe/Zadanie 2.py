n = int(input("Podaj liczbę wyrazów: "))
tablica = [0] * n

for i in range(n):
    tablica[i] = input(f"Wprowadź {i + 1} wyraz: ")

min = min(len(wyraz) for wyraz in tablica)
max = max(len(wyraz) for wyraz in tablica)

liczniki = [[] for _ in range(max - min + 1)]

for i in range(n):
    liczniki[len(tablica[i]) - min].append(tablica[i])

j = 0

for i in range(len(liczniki)):
    while len(liczniki[i]) > 0:
        tablica[j] = liczniki[i][0]
        liczniki[i] = liczniki[i][1:]
        j += 1

print(tablica)
