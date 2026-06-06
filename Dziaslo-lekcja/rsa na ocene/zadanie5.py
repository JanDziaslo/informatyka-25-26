plik = open("tajny-tekst.txt", "r")
tekst = plik.read()
plik.close()

if len(tekst) % 2 == 1:
    tekst += " "

wynik = []
for i in range(0, len(tekst), 2):
    m = (ord(tekst[i]) % 128) * 128 + (ord(tekst[i + 1]) % 128)
    c = pow(m, 3, 66013)
    wynik.append(str(c))

plik = open("zaszyfrowany_RSA.txt", "w")
plik.write(" ".join(wynik))
plik.close()
