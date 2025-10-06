liczniki = [0] * 10

while True:
    liczba = int(input("Podaj liczbe (0 aby zakonczyc): "))
    if liczba == 0:
        break
    for cyfra in str(liczba):
        liczniki[int(cyfra)] += 1

print("\nWystapienia cyfr:")
for i in range(10):
    if liczniki[i] > 0:
        print(f"Cyfra {i}: {liczniki[i]}")

