def monety(kwota, nominaly, sztuki):
    count = 0
    for nominal, dostepne in zip(nominaly, sztuki):
        ile = min(kwota // nominal, dostepne)
        count += ile
        kwota -= ile * nominal
    return count


print(monety(11, [20, 10, 5, 2, 1], [100, 100, 100, 100, 100]))
print(monety(99, [20, 10, 5, 1], [1, 10, 1, 10]))