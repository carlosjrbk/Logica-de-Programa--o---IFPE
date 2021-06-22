sq = 0
vl = 0.0
tl = 0.0
idade=1
print('para sai e encerrar a conta digite (0)')
print('')
while (idade > 0):
    idade = int(input("INFORME A IDADE: "))
    sq += 1
    tl += float(vl)
    if idade == 0:
        print('PROGRAMA ENCERRADO')
        break
    elif (idade == 1):
        vl = 0.00
        print('ENTRADA GRATUITA')
    elif (idade == 2):
        vl = 0.00
        print('ENTRADA GRATUITA')
    elif (idade > 2) and (idade <= 12):
        vl = 10.00
        print("VALOR DO INGRESSO R$:", float(vl))
    elif (idade >= 65):
        vl = 0.00
        print('ENTRADA GRATUITA')
    elif(idade < 65) and (idade > 12):
        vl = 20.00
        print("VALOR DO INGRESSO R$:", float(vl))
        
print("TOTAL A PAGAR PELAS ENTRADAS: " + str(tl))
        