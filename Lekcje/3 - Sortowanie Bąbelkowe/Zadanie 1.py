n = 20

tablica = []

for i in range(n):
    tablica.append(int(input(f"Podaj {i+1} element tablicy: ")))

for j in range(0, n - 1):
    for i in range(0, n - 1):
        if tablica[i] > tablica[i + 1]:
            tablica[i], tablica[i + 1] = tablica[i + 1], tablica[i]

print(tablica)