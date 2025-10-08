#Napisz program, który sprawdzi, czy dwa słowa są anagramami. Program powinien wczytać dane z pliku
#tekstowego. W zapisie słów mogą wystąpić litery z polskiego alfabetu.

with open("dane_12.txt", "r", encoding="utf-8") as plik:
    slowo1 = plik.readline().strip()
    slowo2 = plik.readline().strip()

if sorted(slowo1.lower()) == sorted(slowo2.lower()):
    print("Słowa są anagramami.")
else:
    print("Słowa nie są anagramami.")
