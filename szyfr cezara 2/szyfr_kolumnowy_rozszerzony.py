tekst = input("Podaj tekst: ")
klucz_str = input("Podaj klucz (liczby oddzielone spacjami, np. 3 1 4 2): ")
klucz = [int(x) for x in klucz_str.split()]

kolumny = len(klucz)
wiersze = (len(tekst) + kolumny - 1) // kolumny

macierz = [[' ' for _ in range(kolumny)] for _ in range(wiersze)]

index = 0
for i in range(wiersze):
    for j in range(kolumny):
        if index < len(tekst):
            macierz[i][j] = tekst[index]
            index += 1

zaszyfrowany = ""
for pozycja in klucz:
    kolumna = pozycja - 1
    for i in range(wiersze):
        zaszyfrowany += macierz[i][kolumna]

print("Zaszyfrowany tekst:", zaszyfrowany)
