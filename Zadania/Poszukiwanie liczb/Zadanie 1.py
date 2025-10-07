# Napisz program, który sprawdzi, czy dana liczba znajduje się w tablicy n liczb całkowitych. Wykorzystaj
# funkcję realizującą algorytm przeszukiwania liniowego.
# Wynikiem funkcji powinna być pozycja szukanego elementu lub wartość n, jeśli elementu nie ma w
# tablicy.

n = int(input("Podaj rozmiar tablicy: "))
tablica = [0] * n

for i in range(n - 1):
    tablica[i] = i

liczba = int(input("Podaj liczbę do sprawdzenia: "))

for i in range(len(tablica)):
    if tablica[i] == liczba:
        print(f"Znaleziono liczbę, znajduje się ona na indeksie {i}")