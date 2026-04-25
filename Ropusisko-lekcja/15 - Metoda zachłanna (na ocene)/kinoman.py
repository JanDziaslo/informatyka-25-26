# Tu jest sam algorytm, reszta to taka otoczka jakby ktoś chciał interaktywnie wprowadzać dane, albo użyć danych testowych (ułatwia testowanie algorytmu).

# Dane wejściowe: Lista filmów, czas rozpoczęcia i zakończenia.
# Wynik: Lista filmów, które można obejrzeć.
# Warunek: Filmy nie moga się na siebie nakładać czasowo (czyli nie można zacząć oglądać filmu jeżeli poprzedni się nie skończył)


def kinoman(filmy):
    if not filmy:
        return []

    posortowane = sorted(filmy, key=lambda x: x[2])

    wybrane = [posortowane[0]]

    for film in posortowane[1:]:
        if film[1] >= wybrane[-1][2]:
            wybrane.append(film)

    return wybrane

# =============

def przetworz_czas(czas_str):
    czesci = czas_str.split(':')
    return int(czesci[0]) * 60 + int(czesci[1])

def dodaj_film():

    if not filmy:
        id_filmu = 1
    else:
        id_filmu = filmy[-1][0] + 1

    rozpoczecie = przetworz_czas(input("Podaj czas rozpoczęcia filmu (GG:MM): "))
    zakonczenie = przetworz_czas(input("Podaj czas zakończenia filmu (GG:MM): "))

    filmy.append((id_filmu, rozpoczecie, zakonczenie))

filmy = []

print()
print("Metoda zachłanna (kinoman): ")
print("Dane wejściowe: Lista filmów, czas rozpoczęcia i zakończenia.")
print("Wynik: Lista filmów, które można obejrzeć.")
print("Warunek: Filmy nie moga się na siebie nakładać czasowo (czyli nie można zacząć oglądać filmu jeżeli poprzedni się nie skończył).")
print()

print("1. Wprowadź filmy samemu")
print("2. Użyj danych testowych")

wybor = int(input("Wybór: "))

if wybor == 2:
    testowe = [
        (1, 540, 600),
        (2, 570, 660),
        (3, 600, 690),
        (4, 660, 750),
        (5, 690, 780),
        (6, 780, 870)
    ]

    for f in testowe:
        filmy.append(f)

while True:

    print(f"Dodane filmy: ")

    for i in range(len(filmy)):
        s, k = filmy[i][1], filmy[i][2]
        print(f"  Film {i+1}: {s//60:02d}:{s%60:02d} - {k//60:02d}:{k%60:02d}")

    print()
    print("Co chcesz zrobić?")
    print("1. Dodaj nowy film")
    print("2. Zakończ wprowadzanie filmów")
    wybor = int(input("Wybór: "))

    if wybor == 1:
        dodaj_film()
    else:
        break

wynik = kinoman(filmy)

print(f"Wybrano {len(wynik)} filmów:")

for fid, s, k in wynik:
    print(f"  Film {fid}: {s//60:02d}h:{s%60:02d}m – {k//60:02d}h:{k%60:02d}m")