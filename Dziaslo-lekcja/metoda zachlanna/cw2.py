def wiele(kwota):
    count = 0
    for nominal in [20, 10, 5, 2, 1]:
        count += kwota // nominal
        kwota %= nominal
    return count

print(wiele(11))
print(wiele(99))
