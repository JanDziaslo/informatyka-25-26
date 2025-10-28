import random

def SzukajLin(A,x):
    for i in range(len(A)):
        if A[i] == x:
            return True
    return False

tablica = [random.randint(1,100) for _ in range(10)]
print("Wygenerowana tablica:", tablica)
liczba = int(input("Podaj liczbę do wyszukania: "))
if SzukajLin(tablica,liczba):
    print("Liczba znajduje się w tablicy.")
else:
    print("Liczba nie znajduje się w tablicy.")
