# Tu jest sam algorytm, reszta to taka otoczka jakby ktoś chciał interaktywnie wprowadzać dane, albo użyć danych testowych (ułatwia testowanie algorytmu).

# Dane wejściowe: Lista zawodników z wagami, maksymalna waga pary.
# Wynik: Lista par, które można utworzyć.
# Warunek: Suma wag pary nie może przekroczyć maksymalnej wagi.

def maks_par(wagi, maks_waga):
    if not wagi or maks_waga <= 0:
        return []

    posortowane = sorted(wagi)

    pary = []
    lewo, prawo = 0, len(posortowane) - 1

    while lewo < prawo:
        # Jeżeli najlżejszy + najcięższy < maksymalna waga, to robimy parę
        if posortowane[lewo] + posortowane[prawo] <= maks_waga:
            pary.append((posortowane[lewo], posortowane[prawo]))
            lewo += 1
            prawo -= 1
        # Jak nie to usuwamy najcięższego bo i tak z nim nie utworzymy pary
        else:
            prawo -= 1

    return pary

# ========

def dodaj_zawodnika():
    if not zawodnicy:
        id_zaw = 1
    else:
        id_zaw = zawodnicy[-1][0] + 1

    waga = int(input("Podaj wage zawodnika (kg): "))
    zawodnicy.append((id_zaw, waga))


zawodnicy = []

print()
print("Metoda zachłanna (pary sportowe): ")
print("Dane wejściowe: Lista zawodników z wagami, maksymalna waga pary.")
print("Wynik: Lista par, które można utworzyć.")
print("Warunek: Suma wag pary nie może przekroczyć maksymalnej wagi.")
print()

print("1. Wprowadź zawodników samemu")
print("2. Użyj danych testowych")

wybor = int(input("Wybór: "))

if wybor == 2:
    testowe = [(1, 70), (2, 73), (3, 65), (4, 80), (5, 55), (6, 90), (7, 60), (8, 75)]
    for zawodnik in testowe:
        zawodnicy.append(zawodnik)

max_waga = int(input("Podaj maksymalną wage pary (kg): "))

while True:
    print(f"Dodani zawodnicy: ")

    for i in range(len(zawodnicy)):
        w = zawodnicy[i][1]
        print(f"  Zawodnik {i+1}: {w} kg")

    print()
    print("Co chcesz zrobić?")
    print("1. Dodaj nowego zawodnika")
    print("2. Zakończ wprowadzanie zawodników")
    wybor = int(input("Wybór: "))

    if wybor == 1:
        dodaj_zawodnika()
    else:
        break

wagi = [w for _, w in zawodnicy]
wynik = maks_par(wagi, max_waga)

print(f"\nUtworzono {len(wynik)} par:")

for i, (pierwszy, drugi) in enumerate(wynik):

    print(f"  Para {i+1}: {pierwszy} kg + {drugi} kg = {pierwszy + drugi} kg")

niewykorzystani = len(wagi) - len(wynik) * 2

if niewykorzystani > 0:
    print(f"Niewykorzystani zawodnicy: {niewykorzystani}")