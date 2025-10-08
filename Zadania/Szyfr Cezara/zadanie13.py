#Napisz program wczytujący dowolny tekst z klawiatury oraz liczbę będącą kluczem szyfrowania (liczbę kolumn).
#Program powinien szyfrować wczytany tekst szyfrem przestawieniowym polegającym na spiralnym odczytaniu
#tekstu jawnego zapisanego wierszami
import math

tekst_jawny = input("Podaj tekst: ").replace(" ", "")
klucz = int(input("Podaj klucz: "))

wiersze = math.ceil(len(tekst_jawny) / klucz)
tekst_jawny += 'X' * (wiersze * klucz - len(tekst_jawny))

macierz = [list(tekst_jawny[i * klucz:(i + 1) * klucz]) for i in range(wiersze)]

spirala = [
    (1, 1), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0),
    (2, 0), (2, 1), (1, 2), (0, 3), (0, 2), (0, 1),
    (0, 0), (1, 0), (2, 2), (1, 3), (1, 0)
]

szyfrogram = ''.join(macierz[w][k] for w, k in spirala)

print(szyfrogram)
