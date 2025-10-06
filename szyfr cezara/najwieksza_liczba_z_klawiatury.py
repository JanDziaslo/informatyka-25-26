maksimum = 0

while True:
    liczba = int(input("Podaj liczbe (0 aby zakonczyc): "))
    if liczba == 0:
        break
    if liczba > maksimum:
        maksimum = liczba

print(f"Najwieksza liczba: {maksimum}")

