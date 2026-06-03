def deszyfrowanie_rsa(liczba):
    w = 1

    # Tutaj zakladamy ze klucz jest stały i jest (43667, 66013)
    # czyli tak jak prosili w zadaniu

    wykladnik = 43667
    n = 66013

    while wykladnik > 0:
        if wykladnik % 2 == 1:
            w = (w * liczba) % n
        wykladnik //= 2
        if wykladnik > 0:
            liczba = (liczba * liczba) % n

    return w

tekst = []

with open("tajny-szyfrogram.txt", "r") as plik:
    liczby = plik.read().split()

for i in range(len(liczby)):

    liczba = int(liczby[i])

    znak_odszyfrowany = deszyfrowanie_rsa(liczba)

    znak1 = chr(znak_odszyfrowany // 256)
    znak2 = chr(znak_odszyfrowany % 256)

    tekst.append(znak1)
    tekst.append(znak2)

odszyfrowany = "".join(tekst)

with open("tajny_odszyfrowany.txt", "w") as plik:
    plik.write(odszyfrowany)

