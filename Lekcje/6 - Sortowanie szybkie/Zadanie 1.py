def sortowanie(lewy, prawy):
    if lewy >= prawy:
        return

    i = lewy
    j = prawy
    pivot = tablica[(lewy + prawy) // 2]

    while i <= j:
        while tablica[i] < pivot:
            i += 1
        while tablica[j] > pivot:
            j -= 1
        if i <= j:
            tablica[i], tablica[j] = tablica[j], tablica[i]
            i += 1
            j -= 1

    if lewy < j:
        sortowanie(lewy, j)
    if i < prawy:
        sortowanie(i, prawy)

n = int(input("Podaj liczbę elementów: "))
tablica = []

for i in range(n):
    tablica.append(int(input(f"Wprowadź {i + 1} element: ")))

sortowanie(0, n - 1)
print(tablica)
