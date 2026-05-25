def karp_rabin(tekst, wzorzec):
    n, m = len(tekst), len(wzorzec)
    if m > n: return -1
    hw = sum(ord(c) for c in wzorzec)
    ht = sum(ord(tekst[i]) for i in range(m))
    pozycje = []
    for i in range(n - m + 1):
        if ht == hw and tekst[i:i+m] == wzorzec:
            pozycje.append(i)
        if i + m < n:
            ht = ht - ord(tekst[i]) + ord(tekst[i + m])
    return pozycje if pozycje else -1
