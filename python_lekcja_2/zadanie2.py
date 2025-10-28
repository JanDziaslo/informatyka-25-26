import random


def SzukajBin(A, x):
    lewy = 0
    prawy = len(A) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if A[srodek] == x:
            return srodek + 1
        elif A[srodek] < x:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return 0

def Sortuj(A):
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


n = int(input("Podaj liczbę elementów tablicy: "))
tablica = [random.randint(1,2137) for _ in range(n)]

Sortuj(tablica)
print("Wygenerowana tablica:", tablica)

szukany = int(input("Podaj szukany element: "))

wynik = SzukajBin(tablica, szukany)

if wynik != 0:
    print(f"Element {szukany} znaleziony na pozycji {wynik}")
else:
    print(f"Element {szukany} nie występuje w tablicy")
