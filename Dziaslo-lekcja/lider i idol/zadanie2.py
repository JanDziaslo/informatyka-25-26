def szukaj_lidera(A):
    n = len(A)
    A = sorted(A)
    kandydat = A[n // 2]
    ile = 0
    for i in range(n):
        if A[i] == kandydat:
            ile += 1
    if ile > n // 2:
        return kandydat
    return "nie ma kandydata"


L = [1, 2, 3, 4, 2, 2, 2]
print(szukaj_lidera(L))
