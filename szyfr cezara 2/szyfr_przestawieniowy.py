tekst = input("Podaj tekst do zaszyfrowania: ")

zaszyfrowany = ""
for i in range(0, len(tekst) - 1, 2):
    zaszyfrowany += tekst[i + 1]
    zaszyfrowany += tekst[i]

if len(tekst) % 2 == 1:
    zaszyfrowany += tekst[-1]

print("Zaszyfrowany tekst:", zaszyfrowany)
