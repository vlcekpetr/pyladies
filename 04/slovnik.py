kosik = {"jablko": "cervene", "hruska": "zelena", "broskev": "oranzova", "banan": "zluty"}
snily_kosik = dict(kosik)
for ovoce, barva in snily_kosik.items():
    snily_kosik[ovoce] = 'hnědo-{}'.format(barva)


print(snily_kosik["broskev"])