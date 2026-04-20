waga_plecaka = int(input("Podaj W: "))

if waga_plecaka <= 0:
    print("Waga plecaka nie może być mniejsza niż 1!")
    exit(1)

przedmioty = []
wag = []
wart = []

print("Podawaj dane przedmiotów (liczba -1 kończy):")
while True:
    liczba_przedmiotow = int(input("Podaj ilość przedmiotów (-1 kończy wpisywanie): "))
    if liczba_przedmiotow == -1:
        break
    if liczba_przedmiotow <= 0:
        print("Liczba przedmiotów musi być dodatnia!")
        continue

    przed_waga = int(input("Podaj wagę przedmiotu (jednej sztuki): "))
    przed_wart = int(input("Podaj wartość przedmiotu (jednej sztuki): "))
    wag.append(przed_waga)
    wart.append(przed_wart)
    przedmioty.append(liczba_przedmiotow)

n = len(wag)

if n == 0:
    print("Brak przedmiotów!")
    exit(0)

strategia = int(input("Wybierz strategię (1-wartość, 2-waga, 3-gęstość): "))

if strategia == 1:
    kolejnosc = sorted(range(n), key=lambda i: wart[i], reverse=True)
elif strategia == 2:
    kolejnosc = sorted(range(n), key=lambda i: wag[i])
elif strategia == 3:
    kolejnosc = sorted(range(n), key=lambda i: wart[i]/wag[i] if wag[i] > 0 else 0, reverse=True)
else:
    print("Nieprawidłowa strategia!")
    exit(1)

pozostalo = waga_plecaka
wartosc = 0

print("\nWynik:")
for i in kolejnosc:
    max_ile = przedmioty[i]
    ile = min(max_ile, pozostalo // wag[i])
    if ile > 0:
        wartosc += ile * wart[i]
        pozostalo -= ile * wag[i]
        print(f"Przedmiot {i+1}: {ile} szt. (waga {ile*wag[i]}, wartość {ile*wart[i]})")

print(f"\nŁączna wartość = {wartosc}")
print(f"Zajęto: {waga_plecaka - pozostalo} z {waga_plecaka} kg Maks plecaka, zostało: {pozostalo} kg wolnego.")