lista = ["jeden", 2, 3, 4, 5]

print("1. Dodanie elementów")
lista.append(6)

lista.insert(0, "zero")

lista.insert(2, "trzecia pozycja")

print(lista)

print("2. Usuniecie indeksu 1")
lista.pop(1)

print(lista)

print("3. Zastąpienie 3")
lista[4] = "pies"

print(lista)