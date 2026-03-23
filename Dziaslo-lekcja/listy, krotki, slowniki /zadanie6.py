def zlicz_wystapienia(sekwencja):
    wynik = {}
    for elem in sekwencja:
        wynik[elem] = wynik.get(elem, 0) + 1
    return wynik

przyklad = [3, 1, 2, 1, 3, 3, 5, 2, 1]
wynik = zlicz_wystapienia(przyklad)

for elem in sorted(wynik):
    print(f'{elem}: {wynik[elem]}')
