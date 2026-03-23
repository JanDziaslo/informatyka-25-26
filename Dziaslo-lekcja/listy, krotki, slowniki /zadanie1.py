lista = [10, 'Adam', 3.14, True, 'kot']
print('Oryginalna lista:', lista)

lista.append('koniec')
lista.insert(0, 'poczatek')
lista.insert(2, 'trzecia')
print('Po dodaniu elementów:', lista)

lista.pop(1)
print('Po usunięciu indeksu 1:', lista)

lista[4] = 'pies'
print('Po zamianie indeksu 4:', lista)

print("Tak, wszystkie operacje wykonane pomyślnie.")