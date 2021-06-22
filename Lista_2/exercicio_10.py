print('='*80)
print('    ------------------CODIGO E PREÇOS  DOS COMBUSTIVEIS------------------')
print('='*80)
print('COMBUSTIVEL -----------COD--------PREÇO ATE 20Lt------PREÇO ACIMA DE 20 Lt')
print('ALCOOL                  1           R$ 3.16                  R$ 3.14')
print('GASOLINA                2           R$ 4.20                  R$ 4.19')
print('')
pc = input('INFORME A QUANTIDADE EM LITROS DE COMBUSTIVEL : ')
pc = pc.replace(",",".")
pc = float(pc)
cod = float(input('INFORME O CODIGO DO COMBUSTIVEL: '))
print('')

if cod == 1 and pc <=20:
    valor = (3.16 * pc)
    print('VOCE DEVERÁ PAGAR DE ALCOOL:  R$%4.2f' %(valor))
elif cod ==1 and pc >=21:
    valor = (3.14 * pc)
    print('VOCE DEVERÁ PAGAR DE ALCOOL: R$%4.2f' %(valor))
elif cod == 2 and pc <=20:
    valor = (4.20 * pc)
    print('VOCE DEVERÁ PAGAR DE GASOLINA:  R$%4.2f' %(valor))
elif cod == 2 and pc >=21:
    valor = (4.19 * pc)
    print('VOCE DEVERÁ PAGAR DE GASOLINA:  R$%4.2f' %(valor))
else:
    print('ERRO DE DIGITAÇÃO')






