# Napisz program, który sprawdzi, czy dana liczba znajduje się w uporządkowanej tablicy n liczb
# całkowitych. Wykorzystaj funkcję realizującą algorytm przeszukiwania binarnego. Wynikiem funkcji
# powinna być pozycja szukanego elementu lub wartość n, jeśli szukanego elementu nie ma w tablicy.

n = int(input("Podaj n: "))

tablica = [0] * n

for i in range(n):
    tablica[i] = int(input(f"Podaj {i+1} liczbę: "))

tablica.sort()
liczba = int(input("Podaj liczbę do sprawdzenia: "))

lewy = 0
prawy = n - 1

while lewy <= prawy:
    srodek = (lewy + prawy) // 2
    if tablica[srodek] == liczba:
        print(f"Znaleziono liczbę, znajduje się ona na indeksie {srodek}")
        break
    elif tablica[srodek] < liczba:
        lewy = srodek + 1
    else:
        prawy = srodek - 1

