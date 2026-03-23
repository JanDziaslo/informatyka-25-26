tup = (10, 'Adam', 3.14, True, 'kot')
print('Oryginalna krotka:', tup)

tup = tup + ('koniec',)
tup = ('poczatek',) + tup
tup = tup[:2] + ('trzecia',) + tup[2:]
print('Po dodaniu elementów:', tup)

tup = tup[:1] + tup[2:]
print('Po usunięciu indeksu 1:', tup)

tup = tup[:4] + ('pies',) + tup[5:]
print('Po zamianie indeksu 4:', tup)

print('\nWszystkie operacje wykonane, ale zawsze tworzona była NOWA krotka.')
