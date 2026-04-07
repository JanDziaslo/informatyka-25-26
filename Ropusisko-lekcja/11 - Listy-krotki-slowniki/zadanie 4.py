n = int(input('Podaj liczbę imion: '))
imiona = []

for i in range(n):
    imiona.append(input(f'Podaj {i + 1 } imię: '))

print("Słownik")
slownik = {}

for imie in imiona:
    slownik[imie] = slownik.get(imie, 0) + 1

for imie in sorted(slownik):
    print(f'{imie}: {slownik[imie]}')

print()

print("Lista")
for imie in sorted(set(imiona)):
    print(f'{imie}: {imiona.count(imie)}')
