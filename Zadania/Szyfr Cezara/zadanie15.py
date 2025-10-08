#Napisz program, który z pliku tekstowego przekazanego przez nauczyciela (np.
#szyfrogram_kolumnowy.txt) wczyta jednowierszowy szyfrogram i klucz szyfrowania.
#Szyfrogram powstał przez zaszyfrowanie tekstu jawnego szyfrem kolumnowym. Klucz (drugi wiersz pliku) jest
#napisem złożonym z niepowtarzających się cyfr dziesiętnych mniejszych od drugości klucza i określa liczbę
#kolumn oraz kolejność ich przeglądania.
#Wynikiem działania programu powinien być tekst jawny wyświetlony na ekranie

with open("szyfrogram_kolumnowy.txt", "r", encoding="utf-8") as plik:
    szyfrogram = plik.readline().strip()
    klucz = plik.readline().strip()

liczba_kolumn = len(klucz)
liczba_wierszy = len(szyfrogram) // liczba_kolumn

kolejnosc = [int(znak) - 1 for znak in klucz]

kolumny = []
pozycja = 0
for i in range(liczba_kolumn):
    kolumna = []
    for w in range(liczba_wierszy):
        kolumna.append(szyfrogram[pozycja])
        pozycja += 1
    kolumny.append(kolumna)

tabela = [[""] * liczba_kolumn for _ in range(liczba_wierszy)]
for i, pos in enumerate(kolejnosc):
    for w in range(liczba_wierszy):
        tabela[w][pos] = kolumny[i][w]

tekst_jawny = ""
for w in range(liczba_wierszy):
    for k in range(liczba_kolumn):
        tekst_jawny += tabela[w][k]

print("Tekst jawny:", tekst_jawny)
