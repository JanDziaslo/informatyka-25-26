def szukaj_wzorca(tekst, wzorzec):
    n, m = len(tekst), len(wzorzec)
    pozycje = []
    for i in range(n - m + 1):
        if tekst[i:i+m] == wzorzec:
            pozycje.append(i)
    return pozycje if pozycje else -1
