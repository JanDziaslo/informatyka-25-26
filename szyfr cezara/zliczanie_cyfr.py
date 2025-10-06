liczba = int(input("Podaj liczbe: "))

liczniki = [0] * 10

for cyfra in str(liczba):
    liczniki[int(cyfra)] += 1

for i in range(10):
    if liczniki[i] > 0:
        print(f"Cyfra {i}: {liczniki[i]}")

