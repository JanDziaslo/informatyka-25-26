produkty = {
    'produkt1': 92.40,
    'produkt2': 38.90,
    'produkt3': 111.25,
    'produkt4': 29.99,
    'produkt5': 68.10,
    'produkt6': 104.75,
    'produkt7': 18.60,
    'produkt8': 57.80,
    'produkt9': 189.90,
    'produkt10': 9.99
}

posortowane = sorted(produkty.items(), key=lambda x: x[1], reverse=True)

print('3 najdroższe:')
for nazwa, cena in posortowane[:3]:
    print(f'{nazwa} {cena}')

print('\n3 najtańsze:')
posortowane = posortowane[::-1]

for nazwa, cena in posortowane[:3]:
    print(f'{nazwa} {cena}')

print(f'\nŚrednia cena: {sum(produkty.values()) / len(produkty):.2f}')
