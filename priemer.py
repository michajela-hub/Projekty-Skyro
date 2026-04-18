pocet = int(input("Zadaj počet čísel: "))
sucet = 0

for i in range(pocet):
    cislo = float(input("Zadaj číslo: "))
    sucet += cislo

print("Priemer je:", sucet / pocet)