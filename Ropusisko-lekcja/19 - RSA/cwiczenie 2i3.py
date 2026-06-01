def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nwd_rozszerzony(a, b):
    if b == 0:
        return 1, 0
    x1, y1 = nwd_rozszerzony(b, a % b)
    return y1, x1 - (a // b) * y1


def generuj_klucze_rsa(p, q):
    n = p * q
    m = (p - 1) * (q - 1)

    e = 3
    while nwd(e, m) != 1:
        e += 2

    d, _ = nwd_rozszerzony(e, m)
    if d < 0:
        d += m

    return e, d, n


def rsa(podstawa, wykladnik, n):
    return pow(podstawa, wykladnik, n)


# ćwiczenie 2
p = int(input("Podaj p: "))
q = int(input("Podaj q: "))

e, d, n = generuj_klucze_rsa(p, q)

print("Klucz publiczny:", (e, n))
print("Klucz prywatny:", (d, n))


# ćwiczenie 3
x = 90
y = rsa(x, e, n)
print("Szyfrogram litery Z:", y)