liczby = []
n = 10
print("Wprowadź 10 liczb:")
for i in range(n):
    num = int(input(f"Liczba {i+1}: "))
    liczby.append(num)

print("\nPrzed sortowaniem:", liczby)

for i in range(len(liczby)):
    for j in range(len(liczby) - 1 - i):
        if liczby[j] < liczby[j + 1]:
            liczby[j], liczby[j + 1] = liczby[j + 1], liczby[j]

print("Po sortowaniu:  ", liczby)

