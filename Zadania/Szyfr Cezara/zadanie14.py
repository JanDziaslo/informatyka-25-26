#Napisz program szyfrujący tekst szyfrem kolumnowym z kluczem określającym liczbę kolumn i kolejność ich
#przeglądania tak, aby mogło być więcej niż 10 kolumn.
tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = input("Podaj klucz (np. 3142 dla 4 kolumn): ")

liczba_kolumn = len(klucz)
liczba_wierszy = (len(tekst) + liczba_kolumn - 1) // liczba_kolumn

tekst_dopelniony = tekst + " " * (liczba_wierszy * liczba_kolumn - len(tekst))

tabela = []
for w in range(liczba_wierszy):
    wiersz = []
    for k in range(liczba_kolumn):
        indeks = w * liczba_kolumn + k
        wiersz.append(tekst_dopelniony[indeks])
    tabela.append(wiersz)

kolejnosc = [int(znak) - 1 for znak in klucz]

szyfrogram = ""
for pozycja in kolejnosc:
    for w in range(liczba_wierszy):
        szyfrogram += tabela[w][pozycja]

print("Szyfrogram:", szyfrogram)
