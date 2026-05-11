def szyfruj(slowo, klucz):
    zaszyfrowane = []
    for znak in slowo:
        if znak.isupper():
            nowy_znak = (ord(znak) - ord('A') + klucz) % 26
            zaszyfrowane.append(chr(ord('A') + nowy_znak))
        else:
            nowy_znak = (ord(znak) - ord('a') + klucz) % 26
            zaszyfrowane.append(chr(ord('a') + nowy_znak))
    return ''.join(zaszyfrowane)


with open('slowa1.txt', 'r') as plik_wejsciowy:
    with open('wynik3.txt', 'w') as plik_wyjsciowy:
        for linia in plik_wejsciowy:
            dane = linia.strip().split()
            klucz = int(dane[0])
            slowo = dane[1]
            plik_wyjsciowy.write(szyfruj(slowo, klucz) + '\n')