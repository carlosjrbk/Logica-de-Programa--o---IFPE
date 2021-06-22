f1 = f2 = f3 = f4 = f5 = 0
qtd = int(input('INFORME A QUANTIDADE DE PESSOAS QUE SERÃO ENTREVISTADAS: '))
for cont in range (0, qtd, 1):
    ida = int(input('INFORME SUA IDADE: '))
    if ida >= 0 and ida <= 5:
        f1 += 1
    if ida >= 6 and ida <= 13:
        f2 += 1
    if ida >= 14 and ida <= 17:
        f3 += 1
    if ida >= 18 and ida <= 59:
        f4 += 1
    if  ida >= 60:
        f5 += 1
print('1° faixa (0 - 5) -',f1,'\n2° faixa (6 - 13) -',f2,'\n3° faixa (14 - 17) -',f3,'\n4° faixa (18 - 59) -',f4,'\n5° faixa (60 - a cima) -',f5)
