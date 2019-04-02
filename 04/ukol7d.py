rodne_cislo = '870731/6343'
rok = int(rodne_cislo[:2])
mesic = int(rodne_cislo[2:4])
den = int(rodne_cislo[4:6])

if mesic > 50:
    pohlavi = "zena"
else:
    pohlavi = "muz"

print(pohlavi)