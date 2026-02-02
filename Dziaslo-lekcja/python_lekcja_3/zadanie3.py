words = ["kot", "informatyka", "dom", "program", "a", "biblioteka", "samochod", "pies", "długopis", "konferencja", "okno", "telefon", "zegar", "krzeslo", "dziadu", "stolica"]

n = len(words)
for i in range(n):
    for j in range(0, n - 1 - i):
        if len(words[j]) > len(words[j + 1]):
            words[j], words[j + 1] = words[j + 1], words[j]

print(words)