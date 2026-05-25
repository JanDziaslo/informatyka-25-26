def szukaj_wzorca(tekst, wzorzec):
    n = len(tekst)
    m = len(wzorzec)
    pozycje = []

    for i in range(n - m + 1):
        if tekst[i:i + m] == wzorzec:
            pozycje.append(i)

    if pozycje:
        return pozycje
    else:
        return -1

tekst = input("Podaj tekst: ")
wzorzec = input("Podaj wzorzec: ")

wynik = szukaj_wzorca(tekst, wzorzec)
if wynik == -1:
    print(-1)
else:
    print(f"Znaleziono na pozycjach: {wynik}")
