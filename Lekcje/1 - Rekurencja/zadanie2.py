def trojkat(n):
    if n == 1:
        return 1
    return n + trojkat(n - 1)

liczba = int(input("Podaj n: "))

print(trojkat(liczba))