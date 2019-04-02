# Tento program rozdává naivní rady do života.
print('Odpovídej "ano" nebo "ne".')

stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano':
    stastna = True
elif stastna_retezec == 'ne':
    stastna = False
else:
    print('Nerozumím!')
    exit()

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
elif bohata_retezec == 'ne':
    bohata = False
else:
    print('Nerozumím!')
    exit()

if bohata:
    if stastna:
        print ("Gratuluji")
    else:
        print ("Zkus se vice usmivat")
else:
    if stastna:
        print ("Zkus vice setrit")
    else:
        print ("Skoc z mostu") 



if stastna:
    if bohata:
        print('Gratuluji.')
    else:
        print('Zkus vice setrit.')
    
elif bohata:
    if stastna:
        print('Gratuluji.')
    else:
        print('Zkus se vice usmivat.')
    
else:
    print('To je mi lito.')