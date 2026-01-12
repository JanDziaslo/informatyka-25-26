import random

def najdluzszy_podciag_dodatni(n):
    tablica = [random.randint(-100, 100) for _ in range(n)]
    print("Wylosowana tablica:", tablica)

    najdluzszy = []
    biezacy = []

    for x in tablica:
        if x > 0:
            if not biezacy or x >= biezacy[-1]:
                biezacy.append(x)
            else:
                if len(biezacy) > len(najdluzszy):
                    najdluzszy = biezacy
                biezacy = [x]
        else:
            if len(biezacy) > len(najdluzszy):
                najdluzszy = biezacy
            biezacy = []

    if len(biezacy) > len(najdluzszy):
        najdluzszy = biezacy

    return najdluzszy

wynik = najdluzszy_podciag_dodatni(1000)
print("Najdłuższy podciąg:", wynik)

