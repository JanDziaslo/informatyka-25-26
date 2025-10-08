n = int(input("Podaj rozmiar tablicy (n): "))

tablica = [0] * n

for i in range(n):
    tablica[i] = int(input(f"Podaj liczbę: {i + 1}: "))

maks = 0

for i in range(n):
    rozmiar = len(str(tablica[i]))
    if rozmiar > maks:
        maks = rozmiar
        liczba = tablica[i]

print("Liczba z największą liczbą cyfr ma:", maks, "cyfr i jest to", liczba)