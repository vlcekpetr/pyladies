def tah_hrace(pole, pozice):
    while True:
        pozice = int(input("vloz cislo od 0 do 19? "))
        if pozice < 0:
            print("tah je mimo hru ")
        elif pole[pozice] != "-":
            print("obsazeno ")
        else:
            return tah(pole, pozice, "o")


print(pozice)