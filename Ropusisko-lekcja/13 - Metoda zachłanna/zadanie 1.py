def zakupy(c, m, z):
    waga_cukru = 2
    waga_maki = 5
    waga_ziemniakow = 12
    
    udzwig_samochodu = 500

    waga_cukru_total = c * waga_cukru
    waga_maki_total = m * waga_maki
    waga_ziemniakow_total = z * waga_ziemniakow

    laczna_waga = waga_cukru_total + waga_maki_total + waga_ziemniakow_total

    return laczna_waga <= udzwig_samochodu

cukier = int(input("Podaj ilość worków cukru: "))
maka = int(input("Podaj ilość worków mąki: "))
ziemniaki = int(input("Podaj ilość worków ziemniaków: "))

print(zakupy(cukier, maka, ziemniaki))