print("Podaj liczby oddzielone spacjami:")
liczby = [int(x) for x in input().split()]

if not liczby:
    print("Brak danych")
else:
    podciagi_rosnace = []
    biezacy = [liczby[0]]

    for i in range(1, len(liczby)):
        if liczby[i] > liczby[i-1]:
            biezacy.append(liczby[i])
        else:
            podciagi_rosnace.append(biezacy)
            biezacy = [liczby[i]]
    podciagi_rosnace.append(biezacy)

    max_dlugosc = max(len(p) for p in podciagi_rosnace)

    najdluzsze = [p for p in podciagi_rosnace if len(p) == max_dlugosc]

    print("Ostatni znaleziony:")
    print(najdluzsze[-1])

    print("Wszystkie:")
    for p in najdluzsze:
        print(p)

