def trzy(kwota):
    
    licznik = 0
    
    while kwota >= 0:
        if kwota >= 5:
            kwota -= 5
            licznik += 1
        elif kwota >= 3:
            kwota -= 3
            licznik += 1
        elif kwota >= 1:
            kwota -= 1
            licznik += 1
        else:
            break
        
    return licznik

kwota = int(input("Podaj kwotę: "))
print(trzy(kwota))