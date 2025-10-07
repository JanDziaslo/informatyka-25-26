# Napisz program, który będzie wczytywał z klawiatury liczby całkowite dodatnie do napotkania zera i wypisywał
# największą z podanych liczb.

maks = 0

liczba = int(input("Podaj liczbe: "))

while liczba != 0:
    if liczba > maks:
        maks = liczba
    liczba = int(input("Podaj liczbe: "))

print("Największą liczbą spośród podanych jest: ", maks)