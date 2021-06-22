qtd = int(input('INFORME A QUANTIDADE DE HABITANTES: '))
maiorid = 0
olida = 0
verdloiro = 0
for n in range(1, qtd + 1):
    ida = int(input('INFORME SUA IDADE: '))
    cab = input('INFORME A COR DO CABELO (CASTANHOS, LOIROS, PRETO): ')
    ol = input('INFORME A COR DE SEUS OLHOS (AZUIS, VERDES, CASTANHOS): ')
    if ol == 'castanhos' and 35 >= ida >= 18 :
            olida += 1
    if ida > maiorid:
            maiorid = ida
    if ol == 'verdes' and cab == 'loiros':
        verdloiro += 1
print('INDIVIDUO DE MAIOR IDADE: ', maiorid)
print('INDIVIDUOS COM IDADE ENTRE 18 E 35 ANOS E DE OLHOS CASTANHOS', olida)
print("INDIVIDUOS COM CABELOS LOIROS E OLHOS VERDES", verdloiro)