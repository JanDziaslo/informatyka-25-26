print("Skrypt był testowany na pythonie 3.14 i na systemie Arch linux")
def pobierz_permutacje(znaki, dlugosc):
    if dlugosc == 0:
        return [""]

    wynik = []
    for idx in range(len(znaki)):
        aktualny = znaki[idx]
        reszta = znaki[:idx] + znaki[idx+1:]
        for perm in pobierz_permutacje(reszta, dlugosc - 1):
            wynik.append(aktualny + perm)

    return wynik


def szukaj_anagramow(slowo):
    slowo = slowo.lower()

    wystapienia = {}
    for znak in slowo:
        if znak in wystapienia:
            wystapienia[znak] += 1
        else:
            wystapienia[znak] = 1

    unikalne_anagramy = set()

    for d in range(3, len(slowo) + 1):
        for p in pobierz_permutacje(list(slowo), d):
            unikalne_anagramy.add(p)

    if slowo in unikalne_anagramy:
        unikalne_anagramy.remove(slowo)

    posortowane = sorted(list(unikalne_anagramy), key=lambda x: (-len(x), x))
    return posortowane, wystapienia


slowo = ""
while len(slowo) < 3:
    slowo = input("Wpisz słowo (min. 3 litery): ").strip()
    if len(slowo) < 3:
        print("Słowo jest za krótkie!")

wyniki, zliczone = szukaj_anagramow(slowo)

print(f"Ilość liter: {zliczone}")
print(f"Liczba anagramów: {len(wyniki)}\n")

#for w in wyniki:
 #   print(w)

with open("anagramy.txt", "w", encoding="utf-8") as f:
    f.write(f"Słowo bazowe: {slowo}\n")
    f.write(f"Zliczone litery: {zliczone}\n")
    for w in wyniki:
        f.write(w + "\n")

print("Zapisano wyniki do anagramy.txt")
