n = int(input("Podaj liczbę elementów: "))
tablica = [0] * n

for i in range(n):
    tablica[i] = int(input(f"Wprowadź {i + 1} element: "))

min = min(tablica)
max = max(tablica)

liczniki = [0] * (max - min + 1)

for i in range(n):
    liczniki[tablica[i] - min] += 1

j = 0

for i in range(len(liczniki)):
    while liczniki[i] > 0:
        tablica[j] = i + min
        liczniki[i] -= 1
        j += 1

print(tablica)
