myslim_na_slovo = input("zadaj slovo:")
print("\n" * 50)
zatial = "_" * len(myslim_na_slovo)
pokusov = 11
while pokusov > 0 and "_" in zatial:
    print(zatial)
    pismeno = input("zadaj pismeno:")
    if pismeno in myslim_na_slovo:
        for i in range(len(myslim_na_slovo)):
            if myslim_na_slovo[i] == pismeno:
                zatial = zatial[:i] + pismeno + zatial[i+1:]
    else:
        pokusov -= 1
        print("nespravne, zostava ti", pokusov, "pokusov")
    if zatial == myslim_na_slovo:
        print("uhadol si slovo", myslim_na_slovo)
        break