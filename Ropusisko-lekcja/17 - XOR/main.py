def szyfruj_slowo(slowo, klucz):
    zaszyfrowany = ""
    for znak in slowo:
        if znak.isupper():

            litera = ord(znak) - ord('A')
            zaszyfrowana_litera = (litera ^ klucz) % 26
            zaszyfrowany += chr(ord('A') + zaszyfrowana_litera)
        elif znak.islower():
            litera = ord(znak) - ord('a')
            zaszyfrowana_litera = (litera ^ klucz) % 26
            zaszyfrowany += chr(ord('a') + zaszyfrowana_litera)
        else:
            zaszyfrowany += znak
    return zaszyfrowany

wyniki = []
with open('slowa1.txt', 'r') as plik:
    for linia in plik:
        
        linia = linia.strip()
        if not linia:
            continue

        czesci = linia.split(' ', 1)

        klucz = int(czesci[0])
        slowo = czesci[1]

        wyniki.append(szyfruj_slowo(slowo, klucz))

with open('wynik4.txt', 'w') as plik:
    for wynik in wyniki:
        plik.write(wynik + '\n')
