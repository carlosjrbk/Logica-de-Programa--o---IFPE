valor = int(input('SEM CONTAR OS CENTAVOS INFORME QUANTOS REAIS VOCE TEM: '))
total = valor 
ced = 200
ced1 = 'Lobo guará'
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'VOCE ESTA LEVANDO NO BOLSO {totalced}  {ced1}')
        if ced == 200:
            ced1 = 'Garoupa' 
            ced = 100
        elif ced == 100:
            
            ced1 = 'Onça'
            ced = 50
        elif ced == 50:
            
            ced1 = 'Mico'
            ced = 20
        elif ced == 20:
            
            ced1 = 'Arara'
            ced = 10
        elif ced == 10:
            
            ced1 = 'Garça'
            ced = 5
        elif ced == 5:
            
            ced1 = 'Tartaruga'
            ced = 2
        totalced = 0
        if total == 0:
            break