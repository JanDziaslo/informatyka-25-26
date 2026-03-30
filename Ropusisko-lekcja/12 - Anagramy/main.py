# Anagramy, zapisywanie do pliku, conajmniej 3 literowe, posortowane według długości i dla danej dlugosci alfabetycznie

import random

def stworz_anagram(slowo):
    from random import randint
    lista = []
    for litera in slowo:
        lista.append(litera)
    anagram = ''
    while lista:
        losowana = randint(0, len(lista) - 1)
        nowa_litera = lista[losowana]
        del(lista[losowana])
        anagram += nowa_litera
    return anagram

def liczenie_liter(slowo):
    wynik = {}
    for litera in slowo:
        wynik[litera] = wynik.get(litera, 0) + 1

    for elem in wynik:
        print(f'{elem}: {wynik[elem]}')

tekst = "zdasdasdasdasdsad"
liczenie_liter(tekst)
anagram = stworz_anagram(tekst)

print(anagram)
