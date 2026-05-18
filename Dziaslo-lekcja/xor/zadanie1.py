with open("slowa1.txt") as f:
    lines = f.readlines()

wynik = []
for line in lines:
    parts = line.strip().split(" ", 1)
    klucz = int(parts[0])
    slowo = parts[1]
    zaszyfrowane = "".join(chr(ord(c) ^ klucz) for c in slowo)
    wynik.append(zaszyfrowane)

with open("wynik4.txt", "w") as f:
    f.write("\n".join(wynik) + "\n")
