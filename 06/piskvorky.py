from random import randrange


def vyhodnot(pole):
    if "xxx" in pole:
        return "vitezi x"
    elif "ooo" in pole:
        return "vitezi o"
    elif "-" not in pole:
        return "plichta"
    else:
        return "-"

def tah(pole, cislo):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:cislo] + symbol + pole[cislo + 1:]

def tah_hrace(pole, pozice, symbol):
    while True:
        pozice = int(input("vloz cislo od 0 do 19? "))
        if pozice < 0 or pozice > 19:
            print("tah je mimo hru ")
        elif pole[pozice] != "-":
            print("obsazeno / hraj znovu ")
        else:
            return tah_hrace(pole, pozice, "o")
    
def tah_pocitace(pole, pozice):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    while True:
        pozice = randrange(0, 20)
        if pole[pozice] == "-":
            return tah(pole, pozice, "x")

def piskvorky1d():
    pole = '-'*20
    while True:
        print(pole)
        pole = tah_hrace(pole)
        pole = tah_pocitace(pole) 
        if vyhodnot(pole) != "-":
            print(vyhodnot(pole))
            break
piskvorky1d()
