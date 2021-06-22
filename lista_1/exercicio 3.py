
print('---------------------------------------');
print('     Calculo de Áreas  Triangulares ');
print('---------------------------------------');

base = float(input(u'Digite a medida em metros da base :\n> '));
print()    
altura = float(input(u'Digite a medida em metros da altura:\n> '));
print()
atr = base * altura;
hect = atr / 10000;
print("A área do terreno triangular é de: %1.2fM\u00b2 que equivale à: %1.4f hectares"%(atr, hect))
import os
os.system("pause")

