slowo1 = input("Podaj pierwsze słowo: ")
slowo2 = input("Podaj drugie słowo: ")
slowo3 = input("Podaj trzecie słowo: ")

if sorted(slowo1) == sorted(slowo2) == sorted(slowo3):
    print("Słowa są anagramami")
else:
    print("Słowa nie są anagramami")
