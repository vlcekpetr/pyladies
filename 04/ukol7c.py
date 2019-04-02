rodne_cislo = '870731/6343'

def datum(rodne_cislo):
    return(int(rodne_cislo[:2]), int(rodne_cislo[2:4]), int(rodne_cislo[4:6]))
print(datum)