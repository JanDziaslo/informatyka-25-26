def trzy(kwota):
    count = 0
    for nominal in [5, 3, 1]:
        count += kwota // nominal
        kwota %= nominal
    return count


print(trzy(11))
print(trzy(99))
