plik = open("tajny-szyfrogram.txt", "r")
liczby = plik.read().split()
plik.close()

d = 43667
n = 66013

tekst = []
for s in liczby:
    x = int(s)
    w = 1
    k = d
    while k > 0:
        if k % 2 == 1:
            w = (w * x) % n
        k //= 2
        if k > 0:
            x = (x * x) % n
    tekst.append(chr(w // 256))
    tekst.append(chr(w % 256))

plik = open("tajny_odszyfrowany.txt", "w")
plik.write("".join(tekst))
plik.close()
