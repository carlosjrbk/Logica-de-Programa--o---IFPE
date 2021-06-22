exp = dec = 0
n = int(input("DIGITE UM NUMERO BINARIO PARA CONVERTER PARA DECIMAL: "))
while n != 0:
    dig = n % 10
    dec = dec + dig * 2 ** exp
    n = n // 10
    exp += 1
print(dec)