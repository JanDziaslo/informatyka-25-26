# Napisz funkcję, która dla danej liczby całkowitej dodatniej znajdzie jej pierwiastek kwadratowy
# dyskretny. Zastosuj algorytm przeszukiwania binarnego.
# Uwaga: Pierwiastek dyskretny z danej liczby to największa liczba całkowita mniejsza lub równa
# pierwiastkowi z tej liczby

n = int(input("Podaj liczbę całkowitą dodatnią: "))

# Przeszukiwanie binarne w zakresie od 0 do n
lewy = 0
prawy = n
wynik = 0

while lewy <= prawy:
    srodek = (lewy + prawy) // 2
    kwadrat = srodek * srodek

    if kwadrat == n:
        # Znaleźliśmy dokładny pierwiastek
        wynik = srodek
    elif kwadrat < n:
        # Kwadrat jest za mały, ale może to być nasz wynik
        wynik = srodek
        lewy = srodek + 1
    else:
        # Kwadrat jest za duży
        prawy = srodek - 1

print(wynik)