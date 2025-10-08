#Napisz program, który wczyta dowolny tekst z klawiatur i zaszyfruje go szyfrem przestawieniowym polegającym
#na zamianie miejscami znaków na pozycjach parzystych i nieparzystych.
tekst = input("Podaj tekst do zaszyfrowania: ")
zaszyfrowany_tekst = ""
for i in range(0, len(tekst)-1, 2):
    zaszyfrowany_tekst += tekst[i+1] + tekst[i]
if len(tekst) % 2 != 0:
    zaszyfrowany_tekst += tekst[-1]
print("Zaszyfrowany tekst:", zaszyfrowany_tekst)
#Przykład: "abcdef" -> "badcfe", "abcde" -> "badce"
