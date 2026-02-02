n = 15

tablica_slowa = []

for i in range(n):
    tablica_slowa.append(input(f"Podaj {i+1} element tablicy: "))

for j in range(0, n - 1):
    for i in range(0, n - 1):
        if len(tablica_slowa[i]) > len(tablica_slowa[i + 1]):
            tablica_slowa[i], tablica_slowa[i + 1] = tablica_slowa[i + 1], tablica_slowa[i]

print(tablica_slowa)