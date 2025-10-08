nazwa_pliku = input("Podaj nazwę pliku: ")

with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
    slowo1 = plik.readline().strip()
    slowo2 = plik.readline().strip()

if sorted(slowo1) == sorted(slowo2):
    print("Słowa są anagramami")
else:
    print("Słowa nie są anagramami")
