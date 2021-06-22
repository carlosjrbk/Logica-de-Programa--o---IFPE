print('='*60)
print('CATEGORIA-------- CODIGIO ---------------MARGEM DE LUCRO')
print()
print('HORTIFRUTI-----------1----------------------------80%---')
print('LATICINIOS-----------2----------------------------80%---')
print('CARNES---------------3---------------------------100%---')
print('PEIXES---------------4---------------------------100%---')
print('AVES-----------------5----------------------------90%---')
print('OVOS-----------------6----------------------------90%---')
print('='*60)
print('')
pc = input('INFORME O PREÇO DE CUSTO DO PRODUTO: ')
pc = pc.replace(",",".")
pc = float(pc)
cod = int(input('INFORME UM CODIGO DA LISTA ACIMA: '))
if cod == 1:
    cod = 0.8
    preco = pc + (pc * cod)
    print('O PREÇO DE VENDA DO PRODUTO É DE: R$:%4.2f' %(preco))
elif cod == 2:
    cod = 0.8
    preco = pc + (pc * cod)
    print('O PREÇO DE VENDA DO PRODUTO É DE: R$:%4.2f' %(preco))
elif cod == 3:
    cod = 1
    preco = pc + (pc * cod)
    print('O PREÇO DE VENDA DO PRODUTO É DE: R$:%4.2f' %(preco))
elif cod == 4:
    cod = 1
    preco = pc + (pc * cod)
    print('O PREÇO DE VENDA DO PRODUTO É DE: R$:%4.2f' %(preco))
elif cod == 5:
    cod = 0.9
    preco = pc + (pc * cod)
    print('O PREÇO DE VENDA DO PRODUTO É DE: R$:%4.2f' %(preco))
elif cod == 6:
    cod = 0.9
    preco = pc + (pc * cod)
    print('O PREÇO DE VENDA DO PRODUTO É DE: R$:%4.2f' %(preco))
elif cod >= 7:
    print('ERRO!! INSIRA UM CODIGO DA TABELA')
