ot = bo = reg = 0
print('*'*35)
print('PESQUISA DE OPINIÃO SOBRE O FILME')
print('*'*35)
for cont in range(1, 21):
    ida = int(input('INFORME SUA IDADE: '))
    print()
    print('OPINIÃO SOBRE O FILME \n 3 - ÓTIMO\n 2 - BOM - \n 1 - REGULAR')
    resp = int(input('->:  '))
    print()
    if resp == 3:
        ot += 1
    if resp == 2:
        bo += 1
    if resp == 1:
        reg += 1
print('RESULTADO \n\nÓTIMO -  ',ot,'PESSOAS''\nBOM -    ',bo,'PESSOAS' '\nREGULAR -',reg,'PESSOAS')