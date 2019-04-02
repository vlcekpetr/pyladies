rodne_cislo = "870731/6343"
zacatek = rodne_cislo[:6]
konec = rodne_cislo[7:] 
zackon = (zacatek + konec)

delitelnost = (zackon) % 11
print(delitelnost)

def delitelnost(zackon, 11):
    if zackon % 11 == 0:
        return True
    else:
        return False
print(delitelnost(zackon,11))

def nejaka_funkce():
	if a > b:
		return True
	else:
		return False

def nejaka_funkce():
	return a > b
