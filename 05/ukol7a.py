rodne_cislo = '870731/6343'

def spravny_format(rodne_cislo):
    return len(rodne_cislo[:6]) == 6 and (rodne_cislo[6:7]) == "/" and len(rodne_cislo[7:]) == 4
print(spravny_format('870731/6343'))



