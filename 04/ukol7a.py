rodne_cislo = '870731/6343'

def zacatek():
	if len(rodne_cislo[:6]) == 6 and (rodne_cislo[6:7]) == '/' and len(rodne_cislo[7:]) == 4:
		return True
	else:
		return False
print(zacatek)