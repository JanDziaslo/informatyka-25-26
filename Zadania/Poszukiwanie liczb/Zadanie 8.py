# Napisz funkcję-, której wynikiem będzie liczba elementów z przedzialu [a; b] (a, b — liczby całkowite, a <
# b), znajdujących się w uporządkowanej niemalejąco tablicy n liczb całkowitych. Zastosuj algorytm
# przeszukiwania binarnego.

def znajdz_pierwsza_pozycje_gte(tablica, wartosc):
    """
    Znajduje pierwszą pozycję elementu >= wartosc w posortowanej tablicy.
    Zwraca indeks lub len(tablica) jeśli wszystkie elementy są mniejsze.
    """
    lewy = 0
    prawy = len(tablica)

    while lewy < prawy:
        srodek = (lewy + prawy) // 2
        if tablica[srodek] < wartosc:
            lewy = srodek + 1
        else:
            prawy = srodek

    return lewy


def znajdz_pierwsza_pozycje_gt(tablica, wartosc):
    """
    Znajduje pierwszą pozycję elementu > wartosc w posortowanej tablicy.
    Zwraca indeks lub len(tablica) jeśli wszystkie elementy są <= wartosc.
    """
    lewy = 0
    prawy = len(tablica)

    while lewy < prawy:
        srodek = (lewy + prawy) // 2
        if tablica[srodek] <= wartosc:
            lewy = srodek + 1
        else:
            prawy = srodek

    return lewy


def zlicz_elementy_w_przedziale(tablica, a, b):
    # Znajdź pierwszą pozycję elementu >= a
    pozycja_start = znajdz_pierwsza_pozycje_gte(tablica, a)

    # Znajdź pierwszą pozycję elementu > b
    pozycja_koniec = znajdz_pierwsza_pozycje_gt(tablica, b)

    # Różnica daje liczbę elementów w przedziale [a, b]
    return pozycja_koniec - pozycja_start


# Przykłady użycia i testy
if __name__ == "__main__":
    # Test 1: Podstawowy przykład
    tablica1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Tablica: {tablica1}")
    print(f"Elementy w przedziale [3, 7]: {zlicz_elementy_w_przedziale(tablica1, 3, 7)}")  # Oczekiwane: 5
    print(f"Elementy w przedziale [1, 10]: {zlicz_elementy_w_przedziale(tablica1, 1, 10)}")  # Oczekiwane: 10
    print(f"Elementy w przedziale [5, 5]: {zlicz_elementy_w_przedziale(tablica1, 5, 5)}")  # Oczekiwane: 1
    print(f"Elementy w przedziale [11, 15]: {zlicz_elementy_w_przedziale(tablica1, 11, 15)}")  # Oczekiwane: 0
    print()

    # Test 2: Tablica z duplikatami
    tablica2 = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]
    print(f"Tablica: {tablica2}")
    print(f"Elementy w przedziale [2, 4]: {zlicz_elementy_w_przedziale(tablica2, 2, 4)}")  # Oczekiwane: 6
    print(f"Elementy w przedziale [5, 5]: {zlicz_elementy_w_przedziale(tablica2, 5, 5)}")  # Oczekiwane: 4
    print()

    # Test 3: Przedział częściowo poza tablicą
    tablica3 = [10, 20, 30, 40, 50]
    print(f"Tablica: {tablica3}")
    print(f"Elementy w przedziale [5, 25]: {zlicz_elementy_w_przedziale(tablica3, 5, 25)}")  # Oczekiwane: 2
    print(f"Elementy w przedziale [15, 35]: {zlicz_elementy_w_przedziale(tablica3, 15, 35)}")  # Oczekiwane: 2
    print()

    # Test 4: Pusta tablica
    tablica4 = []
    print(f"Tablica: {tablica4}")
    print(f"Elementy w przedziale [1, 10]: {zlicz_elementy_w_przedziale(tablica4, 1, 10)}")  # Oczekiwane: 0
