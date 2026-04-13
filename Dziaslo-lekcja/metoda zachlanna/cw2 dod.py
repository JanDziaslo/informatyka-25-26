def zakupy_d2(x, ile):
    count = 0
    for waga in [12, 5, 2]:
        ilosc = min(x // waga, ile)
        count += ilosc
        x -= ilosc * waga
    return count

print(zakupy_d2(127, 9))
print(zakupy_d2(127, 12))