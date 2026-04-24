def pary(wagi, limit):
    wagi.sort()
    l, p, wynik = 0, len(wagi) - 1, 0
    
    while l < p:
        if wagi[l] + wagi[p] <= limit:
            wynik += 1
            l += 1
        p -= 1
        
    return wynik

wagi = [60, 80, 50, 90, 75, 65, 85, 70]
print(f"Liczba par: {pary(wagi, 145)}")
