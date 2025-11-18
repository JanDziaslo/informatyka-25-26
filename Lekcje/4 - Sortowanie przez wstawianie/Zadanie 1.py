def sortowanie_przez_wstawianie(lista, n):
    for i in range(1, n):

        # wstawienie elementu w odpowiednie miejsce
        pom = lista[i]

        # ten element zostanie wstawiony w odpowiednie miejsce
        j = i - 1

        # przesuwanie elementów większych od pom
        while j >= 0 and lista[j] > pom:

             # przesuwanie elementów
             lista[j + 1] = lista[j]
             j -= 1

        lista[j + 1] = pom # wstawienie wartości zmiennej pom w odpowiednie miejsce

n = int(input("Podaj liczbę elementów tablicy: "))

tablica = [0] * n

for i in range(n):
    tablica[i] = int(input(f"Podaj element {i + 1}: "))

sortowanie_przez_wstawianie(tablica, n)
print("Posortowana tablica:")
for i in range(n):
    print(tablica[i], end=" ")