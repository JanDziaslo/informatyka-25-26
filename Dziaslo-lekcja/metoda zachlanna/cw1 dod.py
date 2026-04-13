def zakupy_d1(x):
    count = 0
    for waga in [12, 5, 2]:
        ile = x // waga
        count += ile
        x %= waga
    return count

print(zakupy_d1(127))
print(zakupy_d1(100))
