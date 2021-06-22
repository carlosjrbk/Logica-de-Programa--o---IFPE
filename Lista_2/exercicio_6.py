print('='*30)
print('BRITADEIRA - 130dB\nCORTADOR DE GRAMA - 106dB\nDESPERTADOR - 70dB\nSALA TRANQUILA 70db')
print('='*30)
dcb = int(input('INFORME O NIVEL DE SOM EM DECIBEIS: '))

if dcb == 130:
    print(f'{dcb}dB - nivel de uma  Britadeira')
elif dcb == 106:
    print(f'{dcb}dB - nivel de um cortador de grama')
elif dcb == 70:
    print(f'{dcb}dB - nivel de um despertador ')
elif dcb <= 40:
    print(f'{dcb}dB nivel de sala tranquila ') 
elif 130 < dcb :
    print(f'{dcb}dB nivel maior que uma britadeira')
elif 106 < dcb :
    print(f'{dcb}dB - nivel entre britadeira e cortador de grama')
else:
    70 < dcb 
    print(f'{dcb}dB nivel entre despertador  e cortador de grama')
