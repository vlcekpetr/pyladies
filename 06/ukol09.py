

def vyhodnot(pole):
    if "xxx" in pole:
        return "x vyhrava"
    elif "ooo" in pole:
        return "o vyhrava"
    elif "-" not in pole:
        return "remiza"
    else:
        return "-"

def test_vyhodnot(pole):
    print(pole, vyhodnot(pole))

test_vyhodnot("xoxo")
test_vyhodnot("x--o")
test_vyhodnot("----")
test_vyhodnot("ooox")

#nebo

pole = "xoxo"
print(pole, vyhodnot(pole))

pole = "x--o"
print(pole, vyhodnot(pole))

pole = "----"
print(pole, vyhodnot(pole))

pole = "ooox"
print(pole, vyhodnot(pole))

pole = "ooxo"
print(pole, vyhodnot(pole))