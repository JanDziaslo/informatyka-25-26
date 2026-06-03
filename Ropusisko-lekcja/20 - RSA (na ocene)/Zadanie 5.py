def szyfrowanie_rsa(liczba):
    w = 1

    # Tutaj zakladamy ze klucz jest stały i jest (3, 66013)
    # czyli tak jak prosili w zadaniu

    wykladnik = 3
    n = 66013

    while wykladnik > 0:
        if wykladnik % 2 == 1:
            w = (w * liczba) % n
        wykladnik //= 2
        if wykladnik > 0:
            liczba = (liczba * liczba) % n

    return w

szyfrogram = []

with open("tajny-tekst.txt", "rb") as plik:
    tekst = plik.read()

for i in range(0, len(tekst), 2):

    znak1 = tekst[i]

    if i + 1 < len(tekst):
        znak2 = tekst[i + 1]
    else:
        znak2 = 0

    liczba = znak1 * 256 + znak2
    szyfrogram.append(str(szyfrowanie_rsa(liczba)))

szyfrogram = " ".join(szyfrogram)

with open("zaszyfrowany_RSA.txt", "w") as plik:
    plik.write(szyfrogram)

