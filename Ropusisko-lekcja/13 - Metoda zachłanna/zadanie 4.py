
def monety(kwota, nominaly, sztuki):
    
    licznik = 0
    
    while kwota >= 0:
        for i in range(len(nominaly)):
            
            # Sprawdzanie kwoty i czy mamy ilosc sztuk dla tego nominału
            if kwota >= nominaly[i] and sztuki[i] > 0:
                
                kwota -= nominaly[i]
                sztuki[i] -= 1
                licznik += 1
                break
        else:
            break
        
    return licznik

kwota = int(input("Podaj kwotę: "))

nominal = 1
nominaly = []
sztuki = []

while nominal != 0:
    nominal = int(input("Podaj nominał (0 aby zakończyć): "))
    
    if nominal != 0:
        sztuka = int(input("Podaj liczbę sztuk: "))
        nominaly.append(nominal)    
        sztuki.append(sztuka)

print(monety(kwota, nominaly, sztuki))