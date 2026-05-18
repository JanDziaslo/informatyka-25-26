def szyfruj(tekst, klucz):
    lista = []
    lista[:0] = tekst
    for i in range(len(tekst)):
        lista[i] = chr(ord(lista[i]) ^ klucz)
    return ''.join(lista)


with open("slowa1.txt") as f:
    lines = f.readlines()

wynik = []
for line in lines:
    parts = line.strip().split(" ", 1)
    klucz = int(parts[0])
    slowo = parts[1]
    wynik.append(szyfruj(slowo, klucz))

with open("wynik4.txt", "w") as f:
    f.write("\n".join(wynik) + "\n")
