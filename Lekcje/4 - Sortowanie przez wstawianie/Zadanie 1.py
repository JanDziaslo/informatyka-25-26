n = int(input("Podaj liczbę elementów do posortowania: "))

tablica = [0] * n

for i in range(n):
    tablica[i] = int(input(f"Podaj element {i + 1}: "))

for j in range(n, 1):
    x = tablica[j]
    i = j + i
    while i <= n and tablica[i] < x:
        tablica[i - 1] = tablica[i]
        i = i + 1