def szukaj_lidera(A):
    n = len(A)
    for i in range(n):
        ile = 0
        for j in range(n):
            if A[j] == A[i]:
                ile += 1
        if ile > n // 2:
            return A[i]
    return "nie ma lidera"


L = [1, 2, 3, 4, 2, 2, 2]
print(szukaj_lidera(L))
