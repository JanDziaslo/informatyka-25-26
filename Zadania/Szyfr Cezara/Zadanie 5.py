# Napisz program, który będzie wczytywał z klawiatury liczby całkowite dodatnie do napotkania zera i wypisywał
# liczbę wystąpień poszczególnych cyfr we wszystkich wczytanych liczbach łącznie.

cyfry = "0123456789"
liczniki = [0] * 10

liczby = []
liczba = input("Podaj liczbe: ")

while liczba != "0":
    liczby.append(liczba)
    liczba = input("Podaj liczbe: ")

for liczba in liczby:
    for cyfra in liczba:
        indeks = cyfry.index(cyfra)
        liczniki[indeks] += 1

for i in range(len(cyfry)):
    if liczniki[i] > 0:
        print(f"Cyfra {cyfry[i]} wystepuje {liczniki[i]} razy")