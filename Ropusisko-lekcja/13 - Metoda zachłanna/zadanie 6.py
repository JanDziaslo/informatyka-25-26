def zakupy(udzwig, limit):
    
    licznik_ziemniaki = 0
    licznik_maka = 0
    licznik_cukier = 0
    
    if udzwig < 0:
        return "Udźwig nie może być ujemny."
    
    if udzwig == 0:
        return "Nie można nic kupić, udźwig jest zerowy."
    
    waga_cukier = 2
    waga_maka = 5
    waga_ziemniaki = 12
    
    while udzwig >= waga_ziemniaki and licznik_ziemniaki < limit:
        udzwig -= waga_ziemniaki
        licznik_ziemniaki += 1
    
    while udzwig >= waga_maka and licznik_maka < limit:
        udzwig -= waga_maka
        licznik_maka += 1
    
    while udzwig >= waga_cukier and licznik_cukier < limit:
        udzwig -= waga_cukier
        licznik_cukier += 1
    
    return f"Ziemniaki: {licznik_ziemniaki}, Maka: {licznik_maka}, Cukier: {licznik_cukier}, Łącznie: {licznik_ziemniaki + licznik_maka + licznik_cukier}, Pozostały udźwig: {udzwig}"

udzwig = int(input("Podaj udźwig: "))
limit = int(input("Podaj limit: "))

print(zakupy(udzwig, limit))