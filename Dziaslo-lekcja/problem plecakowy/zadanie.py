n = int(input("Liczba przedmiotow: "))
W = float(input("Pojemnosc plecaka W: "))

p = []
w = []
for i in range(n):
    p.append(float(input(f"p[{i+1}]: ")))
    w.append(float(input(f"w[{i+1}]: ")))

print("\nWybierz strategie:")
print("1 - najcenniejsze (malejaco po p)")
print("2 - najlzejsze (rosnaco po w)")
print("3 - najlepszy stosunek p/w")
s = int(input("Strategia [1/2/3]: "))

if s == 1:
    kolejnosc = sorted(range(n), key=lambda i: p[i], reverse=True)
elif s == 2:
    kolejnosc = sorted(range(n), key=lambda i: w[i])
else:
    kolejnosc = sorted(range(n), key=lambda i: p[i]/w[i], reverse=True)

pozostalo = W
wartosc = 0

print()
for i in kolejnosc:
    ile = int(pozostalo // w[i])
    if ile > 0:
        wartosc += ile * p[i]
        pozostalo -= ile * w[i]
        print(f"Przedmiot {i+1}: {ile} szt. (waga {ile*w[i]}, wartosc {ile*p[i]})")

print(f"\nLaczna wartosc P = {wartosc}")
print(f"Zajeto: {W - pozostalo} / {W} kg, wolne: {pozostalo}")