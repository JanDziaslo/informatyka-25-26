def h(n, r=10):
    return sum(ord(c) for c in n) % r

t = [[] for _ in range(10)]

def dodaj(n, tel):
    b = t[h(n)]
    for i, (x, y) in enumerate(b):
        if x == n: b[i] = (n, tel); return
    b.append((n, tel))

def szukaj(n):
    for x, y in t[h(n)]:
        if x == n: return y
    return -1
