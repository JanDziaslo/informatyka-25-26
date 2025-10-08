# Napisz program, który w tablicy n liczb całkowitych znajdzie pierwszy element parzysty.
# Przyjmij, że w tablicy najpierw występują liczby nieparzyste, potem parzyste oraz że tablica zawiera co
# najmniej jedną liczbę nieparzystą i jedną parzystą. Zastosuj algorytm przeszukiwania binarnego.

tablica = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

lewy = 0
prawy = len(tablica) - 1
wynik = -1

while lewy <= prawy:
    srodek = (lewy + prawy) // 2

    if tablica[srodek] % 2 == 0:  # Element parzysty
        wynik = srodek
        prawy = srodek - 1  # Szukamy dalej po lewej stronie
    else:  # Element nieparzysty
        lewy = srodek + 1  # Szukamy po prawej stronie

print("Tablica:", tablica)
print("Indeks pierwszej liczby parzystej:", wynik)

