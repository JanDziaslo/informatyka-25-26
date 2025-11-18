def trojkaty(n):
    if n == 1:
        return 1
    else:
        return trojkaty(n - 1) +n

opa=int(input("podaj liczbe: "))
print(trojkaty(opa))