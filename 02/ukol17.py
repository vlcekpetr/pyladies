tah_pocitace = 'kamen'
tah_cloveka = input('kamen, nuzky, nebo papir? ')

if tah_pocitace == tah_cloveka:
    print('Plichta')
elif tah_pocitace == 'kamen'and tah_cloveka == 'nuzky' or tah_pocitace == 'papir'and tah_cloveka == 'kamen' or tah_pocitace == 'nuzky'and tah_cloveka == 'papir':
    print('Prohra')
elif tah_pocitace == 'kamen'and tah_cloveka == 'papir' or tah_pocitace == 'papir'and tah_cloveka == 'nuzky' or tah_pocitace == 'nuzky'and tah_cloveka == 'kamen':
    print('Vyhra')
else :
    print ("nerozumim")