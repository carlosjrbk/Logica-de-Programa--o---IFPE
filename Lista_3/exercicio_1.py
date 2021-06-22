x = 1
valor = 0
while x <= 8:
     v = int(input(" Digite o valor número %d: " % x))
     valor = valor + v
     x = x + 1
print("A média aritimetica é: %5.2f" % (valor//8))