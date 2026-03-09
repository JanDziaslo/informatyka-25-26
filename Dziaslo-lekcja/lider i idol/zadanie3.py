def szukaj_lidera(A):
    n = len(A)
    ile = 0
    kandydat = None
    for i in range(n):
        if ile == 0:
            kandydat = A[i]
            ile = 1
        elif A[i] == kandydat:
            ile += 1
        else:
            ile -= 1
    if ile == 0:
        return -1
    ile = 0
    for i in range(n):
        if A[i] == kandydat:
            ile += 1
    if ile > n // 2:
        return kandydat
    return -1


L = [1, 2, 3, 4, 2, 2, 2]
print(szukaj_lidera(L))
