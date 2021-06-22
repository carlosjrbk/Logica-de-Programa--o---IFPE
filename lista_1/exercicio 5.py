
print("-----------------------------------------")

rf = float(input(u'INFORME O VALOR DA REFEIÇÃO:\n->'));
print()
gj = rf * 10/100
print(' ITEM ----- VALOR  \n\n REFEIÇÃO:  R$%1.2f\n GORJETA :  R$%1.2f\n\n TOTAL À PAGAR: R$%1.2f'%( rf , gj, (rf + gj)))


import os
os.system('pause')
