from math import pi
a = 2
b = 4
def obsah_elipsy(delka_a, delka_b):
    "Vrati obvod elipsy"
    return pi * a * b
print(obsah_elipsy(a, b))


def objem_valce(a, b, vyska):
    "Vrati objem eliptickeho valce"
    return obsah_elipsy(a, b) * vyska
print(objem_valce (2, 2, 3))

