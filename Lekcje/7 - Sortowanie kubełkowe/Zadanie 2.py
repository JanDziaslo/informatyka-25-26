n = int(input("Podaj liczbę elementów tablicy: "))

tablica_slowa = []
for i in range(n):
    slowo = input(f"Podaj wyraz {i+1}: ")
    tablica_slowa.append(slowo)

min = min(tablica_slowa)
max = max(tablica_slowa)

kubelki = [[] for _ in range(26)]

for i in range(n):
    pierwsza_litera = tablica_slowa[i][0].lower()
    indeks = ord(pierwsza_litera) - ord('a')
    if 0 <= indeks < 26:
        kubelki[indeks].append(tablica_slowa[i])

j = 0

for i in range(26):
    for slowo in sorted(kubelki[i]):
        tablica_slowa[j] = slowo
        j += 1

print("Posortowana tablica:")
print(tablica_slowa)