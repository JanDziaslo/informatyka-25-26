#Napisz program wczytujący dowolny tekst z klawiatury oraz liczbę będącą kluczem szyfrowania (liczbę kolumn).
#Program powinien szyfrować wczytany tekst szyfrem przestawieniowym polegającym na spiralnym odczytaniu
#tekstu jawnego zapisanego wierszami
tekst = input("Podaj tekst: ")
klucz = int(input("Podaj klucz: "))

slowa = tekst.split()

szyfrogram = []
for slowo in slowa:
    zaszyfrowane = ""
    for znak in slowo:
        if znak.isalpha():
            if znak.isupper():
                nowy = chr((ord(znak) - ord('A') + klucz) % 26 + ord('A'))
            else:
                nowy = chr((ord(znak) - ord('a') + klucz) % 26 + ord('a'))
            zaszyfrowane += nowy
        else:
            zaszyfrowane += znak
    szyfrogram.append(zaszyfrowane)

print("Szyfrogram:", " ".join(szyfrogram))

liczba_kolumn = len(slowa)
liczba_wierszy = max(len(s) for s in szyfrogram)

for w in range(liczba_wierszy):
    for k in range(liczba_kolumn):
        if w < len(szyfrogram[k]):
            print(szyfrogram[k][w], end=" ")
        else:
            print(" ", end=" ")
    print()

