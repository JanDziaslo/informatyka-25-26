# Napisz program wyznaczający rozpiętość zbioru danych znajdujących się w tablicy n liczb całkowitych.

n = int(input("Podaj n: "))

tablica = [0] * n

for i in range(n):
    tablica[i] = int(input(f"Podaj {i+1} liczbę: "))

maks = max(tablica)
min = min(tablica)

print("Rozpiętość zbioru wynosi: ", maks - min)