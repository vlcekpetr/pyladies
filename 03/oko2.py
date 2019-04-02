from random import randrange
print("""Odpovidej ano nebo ne
Snaz se dosahnout souctu 21""")

body = 0
print("Pocet bodu: ", body)
while True:
    odpoved = input('Otocit kartu?')
    if odpoved == 'ano':
        karta = randrange(2, 11)
        soucet = (karta + body)
        print(karta)
        print('Pocet bodu:' (soucet))
    elif odpoved == "ne":
        break
        print('Pocet bodu:' (body))
if soucet <= 21:
    print("Otocit kartu")
elif soucet > 21:
    print("Prohra")