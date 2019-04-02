rodne_cislo = "870731/6343"

def delitelnost(rodne_cislo):
    if ((rodne_cislo[:6])+(rodne_cislo[7:])) % 11 == 0
        return True
    else:
        return False
print(delitelnost(rodne_cislo))