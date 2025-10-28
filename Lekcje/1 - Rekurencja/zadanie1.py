def kwadrat(n):
    if n == 1:
        return 1
    else:
        return kwadrat(n - 1) + 2 * n - 1

liczba = int(input("Podaj n: "))
print(kwadrat(liczba))