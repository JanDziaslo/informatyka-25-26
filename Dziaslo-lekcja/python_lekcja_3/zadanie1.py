liczby = [45, 23, 51, 9, 78, 12, 34, 67, 89, 2, 56, 33, 77, 11, 98, 5, 44, 76, 22, 65]

print("Przed sortowaniem:", liczby)

for i in range(len(liczby)):
    for j in range(len(liczby) - 1 - i):
        if liczby[j] > liczby[j + 1]:
            liczby[j], liczby[j + 1] = liczby[j + 1], liczby[j]

print("Po sortowaniu:  ", liczby)

