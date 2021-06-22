from time import sleep
otm = ot = bo = reg = 0
print('*'*35)
print('PESQUISA DE OPINIÃO SOBRE O FILME')
print('*'*35)
n = int(input('QUANTAS PESSOAS DESEJA ENTREVISTAR?: '))
print()
print("INICIANDO A PESQUISA AGUARDE UM POUCO")
sleep(2)
print()
for cont in range(1, n+1):
    ida = int(input('INFORME SUA IDADE: '))
    print()
    print('OPINIÃO SOBRE O FILME \n 3 - ÓTIMO\n 2 - BOM - \n 1 - REGULAR  \n 4 - ENCERRA A PESQUISA')
    resp = int(input('->:  '))
    print()
    if resp == 3:
        ot += 1
        otm += ida
    if resp == 2:
        bo += 1
    if resp == 1:
        reg += 1
    if resp == 4:
        break
t = ot + reg + bo
p = (bo*100)/t
print("*"*50)
print('RESULTADO DA PESQUISA \n\nÓTIMO -  ',ot,'PESSOAS''\nBOM -    ',bo,'PESSOAS' '\nREGULAR -',reg,'PESSOAS')
print("*"*50)
print('MEDIA DAS IDADES QUE RESPONDERAM ÓTIMO ->',str(otm//ot), 'ANOS')
print('QUANTIDADE DE PESSOAS QUE RESPONDERAM "REGULAR":',reg)
print(f'ENTRE TODOS OS EXPECTADORES: {p:.1f}% RESPONDERAM BOM')
print("*"*50)