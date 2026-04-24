'''
Specyfikacja problemu (Problem kinomana):
Dane: Lista par (krotek) określających czas rozpoczęcia i zakończenia filmów.
Wynik: Maksymalna liczba filmów, które można obejrzeć bez nakładania się na siebie czasów, oraz ich lista.
'''

def kinoman(filmy):
    filmy.sort(key=lambda x: x[1])
    wynik, koniec = [], 0
    
    for s, k in filmy:
        if s >= koniec:
            wynik.append((s, k))
            koniec = k
            
    return wynik

dane = [(10, 12), (11, 13), (12, 14), (13, 15), (14, 16), (15, 17)]
wybrane = kinoman(dane)
print(f"Ilość filmów do obejrzenia: {len(wybrane)}")
print(f"Wybrane filmy: {wybrane}")
