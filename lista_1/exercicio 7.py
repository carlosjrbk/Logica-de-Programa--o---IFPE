
print('========================================================');
print('   "CALCULO DA AREA DO CIRCULO E VOLUME DA ESFERA" ');
print('========================================================');
print();
pi = float(3.1415)
r = float(input(u'INSIRA O RAIO DA CIRCUNFERÊNCIA PARA CALCULAR A ÁREA  E O VOLUME\n-> '));
print()    
ar = pi * r**2
vl =  (4 * pi * r**3)/3
print("A ÁREA DO CIRCULO É DE: %2.2fm\u00b2\n\nO VOLUME DA ESFERA É DE: %2.2fm\u00b3"%(ar, vl))

import os
os.system("pause")


