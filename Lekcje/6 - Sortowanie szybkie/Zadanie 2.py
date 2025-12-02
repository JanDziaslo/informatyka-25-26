def sortowanie(tablica, lewy, prawy):
    if lewy >= prawy:
        return

    i = lewy
    j = prawy
    pivot = len(tablica[(lewy + prawy) // 2])

    while i <= j:
        while len(tablica[i]) < pivot:
            i += 1
        while len(tablica[j]) > pivot:
            j -= 1
        if i <= j:
            tablica[i], tablica[j] = tablica[j], tablica[i]
            i += 1
            j -= 1

    if lewy < j:
        sortowanie(tablica, lewy, j)
    if i < prawy:
        sortowanie(tablica, i, prawy)

n = int(input("Podaj liczbę elementów tablicy: "))

tablica_slowa = [0] * n

for i in range(n):
    tablica_slowa[i] = input(f"Podaj element {i + 1}: ")

sortowanie(tablica_slowa, 0, n - 1)
print("Posortowana tablica:")
for i in range(n):
    print(tablica_slowa[i], end=" ")