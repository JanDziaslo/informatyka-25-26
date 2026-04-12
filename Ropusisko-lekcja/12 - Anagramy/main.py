def generuj_permutacje(litery, dlugosc):

    # Żeby nie trwało w nieskonczonosc
    if dlugosc == 0:
        return [""]

    wyniki = []

    # Tu chodzi o to ze bierzemy pierwszą litere i dla niej robimy permutacje z pozostałymi literami
    # potem bierzemy drugą litere i dla niej robimy permutacje z pozostałymi literami az do konca.

    for i in range(len(litery)):
        litera = litery[i]
        pozostale = litery[:i] + litery[i + 1 :]

        for p in generuj_permutacje(pozostale, dlugosc - 1):
            wyniki.append(litera + p)

    return wyniki


def zrob_anagramy(wyraz):
    wyraz = wyraz.lower()

    licznik = {}
    for litera in wyraz:
        licznik[litera] = licznik.get(litera, 0) + 1

    # Szukanie wszystkich permutacji o długości od 3 do długości słowa

    znalezione = set()

    for i in range(3, len(wyraz) + 1):
        kombinacje = generuj_permutacje(list(wyraz), i)
        for k in kombinacje:
            znalezione.add(k)

    # Wywalamy pierwotny wyraz. Przez discard nie wywala błędu jak wyrazu nie ma.
    znalezione.discard(wyraz)

    # Sortowanie po długości od najdłuższych
    lista_anagramow = list(znalezione)

    # lambda po to, zeby jednocześnie sortować po długości i alfabetycznie w grupie, -len(x) bo chcemy od najwiekszej ilosci liter
    lista_anagramow.sort(key=lambda x: (-len(x), x))

    return lista_anagramow, licznik


wyraz = input("Podaj wyraz (minimum 3 litery): ").strip()

# Sprawdzanie, czy wyraz ma co najmniej 3 litery

while len(wyraz) < 3:
    print("Wyraz jest za krótki!")
    wyraz = input("Podaj wyraz (minimum 3 litery): ").strip()

anagramy, licznik_liter = zrob_anagramy(wyraz)

print(f"Policzone litery: {licznik_liter}")
print(f"Znaleziono {len(anagramy)} anagramów.\n")

# Wyświetlanie wyników
for anagram in anagramy:
    print(anagram)

# zapisanie do pliku

with open("anagramy.txt", "w") as plik:
    plik.write(f"Anagramy dla słowa: {wyraz}\n")
    plik.write(f"Policzone litery: {licznik_liter}\n")

    for anagram in anagramy:
        plik.write(f"{anagram}\n")

print("Anagramy zapisano do pliku anagramy.txt")
