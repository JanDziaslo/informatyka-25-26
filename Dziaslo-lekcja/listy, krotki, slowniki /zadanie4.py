n = int(input('Podaj liczbę imion: '))
imiona = [input(f'Imię {i+1}: ') for i in range(n)]

# Sposób 1: słownik
print('\n--- Słownik ---')
slownik = {}
for imie in imiona:
    slownik[imie] = slownik.get(imie, 0) + 1
for imie in sorted(slownik):
    print(f'{imie}: {slownik[imie]}')

# Sposób 2: lista
print('\n--- Lista ---')
for imie in sorted(set(imiona)):
    print(f'{imie}: {imiona.count(imie)}')
