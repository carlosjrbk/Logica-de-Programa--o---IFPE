x = int(input('informe a quantidade de lados da figura geometrica '))

if x == 3:
    print(f'{x} é um trilatero ')
elif x == 4:
    print(f'{x} é um quadrilatero')
elif x == 5:
    print(f'{x} é um Pentalatero ')
elif x == 6:
    print(f'{x} é um Hexalatero')
elif x == 7:
    print(f'{x} é um Heptalatero')
elif x == 8:
    print(f'{x} é um Octalatero')
elif x == 9:
    print(f'{x} é um Enealatero')
elif x == 10:
    print(f'{x} Decalatero')
else:
    11 <= x <= 2
    print(f'{x} ERRO FORA DO LIMITE')
