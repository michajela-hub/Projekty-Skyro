import random
myslim_cislo = random.randrange(0,10)

for pokus in range(0,3):
    cislo = int(input("Na ake cislo myslim? "))
    if cislo == myslim_cislo:
        print("Uhadol si, gratulujem!")
        break
    elif cislo < myslim_cislo:
        print("Myslim na vacsie cislo")
    else:
        print("Myslim na mensie cislo")
        if pokus == 2:
            print("Prehral si, myslim na", myslim_cislo)