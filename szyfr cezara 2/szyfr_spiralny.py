tekst = input("Podaj tekst: ")
klucz = int(input("Podaj klucz (liczba kolumn): "))

wiersze = (len(tekst) + klucz - 1) // klucz

macierz = []
index = 0
for i in range(wiersze):
    wiersz = []
    for j in range(klucz):
        if index < len(tekst):
            wiersz.append(tekst[index])
        else:
            wiersz.append('X')
        index += 1
    macierz.append(wiersz)

zaszyfrowany = ""
gora = 0
dol = wiersze - 1
lewo = 0
prawo = klucz - 1

while gora <= dol and lewo <= prawo:
    for i in range(lewo, prawo + 1):
        zaszyfrowany += macierz[gora][i]
    gora += 1
    
    for i in range(gora, dol + 1):
        zaszyfrowany += macierz[i][prawo]
    prawo -= 1
    
    if gora <= dol:
        for i in range(prawo, lewo - 1, -1):
            zaszyfrowany += macierz[dol][i]
        dol -= 1
    
    if lewo <= prawo:
        for i in range(dol, gora - 1, -1):
            zaszyfrowany += macierz[i][lewo]
        lewo += 1

print("Zaszyfrowany tekst:", zaszyfrowany)
