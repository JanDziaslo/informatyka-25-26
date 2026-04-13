def wiele(kwota):
    
    licznik = 0
    
    while kwota >= 0:
        if kwota >= 20:
            kwota -= 20
            licznik += 1
        elif kwota >= 10:
            kwota -= 10
            licznik += 1
        elif kwota >= 5:
            kwota -= 5
            licznik += 1
        elif kwota >= 2:
            kwota -= 2
            licznik += 1
        elif kwota >= 1:
            licznik += 1
            
            kwota -= 2
        else:
            break
        
    return licznik

kwota = int(input("Podaj kwotę: "))
print(wiele(kwota))