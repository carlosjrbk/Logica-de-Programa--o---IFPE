
print('--------------------------------------------------------');
print('               CALCULADORA DE MERCADORIA                ');
print('--------------------------------------------------------');


quant = int(input(u'INFORME A QUANTIDADE DA MERCADORIA :\n>'))
q = float(quant)
total = (float(input(u'INFORME O PREÇO UNITARIO:\n>'))) * q
print(u'\nO TOTAL DA COMPRA FOI DE: R$%1.2f'%(total))

import os
os.system("pause")
