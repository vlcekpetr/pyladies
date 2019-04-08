#fc tah, ktera vrati pole s danym symbolem umistenym na danou pozici
def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def test_tah(pole, cislo_policka, symbol):
    print(pole, test_tah)

test_tah(pole, 3, "x")