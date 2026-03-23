produkty = {
    'produkt1': 80.99, 'produkt2': 45.50, 'produkt3': 120.00,
    'produkt4': 33.75, 'produkt5': 75.49, 'produkt6': 99.99,
    'produkt7': 15.00, 'produkt8': 60.25, 'produkt9': 200.00,
    'produkt10': 5.49
}

posortowane = sorted(produkty.items(), key=lambda x: x[1], reverse=True)

print('3 najdroższe:')
for nazwa, cena in posortowane[:3]:
    print(f'{nazwa} {cena}')

print('\n3 najtańsze:')
for nazwa, cena in posortowane[-3:][::-1]:
    print(f'{nazwa} {cena}')

print(f'\nŚrednia cena: {sum(produkty.values()) / len(produkty):.2f}')
