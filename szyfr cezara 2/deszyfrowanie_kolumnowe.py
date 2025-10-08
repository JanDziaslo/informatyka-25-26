nazwa_pliku = input("Podaj nazwę pliku: ")

with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
    szyfrogram = plik.readline().strip()
    klucz_str = plik.readline().strip()

klucz = [int(x) for x in klucz_str.split()]
kolumny = len(klucz)
wiersze = len(szyfrogram) // kolumny

macierz = [['' for _ in range(kolumny)] for _ in range(wiersze)]

index = 0
for pozycja in klucz:
    kolumna = pozycja - 1
    for i in range(wiersze):
        macierz[i][kolumna] = szyfrogram[index]
        index += 1

tekst_jawny = ""
for i in range(wiersze):
    for j in range(kolumny):
        tekst_jawny += macierz[i][j]

print("Tekst jawny:", tekst_jawny)
