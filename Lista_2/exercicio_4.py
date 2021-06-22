num = str(input("INFORME UMA LETRA "))
num = ord(num)
x = chr(num)
if (122 >= num >= 97):
    print(f"esta letra {x} é minuscula")
elif (90 >= num >= 65):
    print(f'esta letra {x} é maiuscula')
else:
    print("ERRO!!! DIGITE UMA LETRA")