# Napisz program, który wczyta liczbę całkowitą większą od zera i wypisze liczbę wystąpień poszczególnych cyfr w tej liczbie.

cyfry = "0123456789"

liczba = input("Podaj liczbe: ")

liczniki = [0] * len(cyfry)

for cyfra in liczba:
    if cyfra in cyfry:
        pozycja = cyfry.index(cyfra)
        liczniki[pozycja] += 1

for i in range(len(cyfry)):
    if liczniki[i] > 0:
        print(f"Cyfra {cyfry[i]} wystepuje {liczniki[i]} razy")