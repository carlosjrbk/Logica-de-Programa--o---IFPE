valores = []
while !=0:
    num = int(input("Digite um numero inteiro: "))
    if num not in valores:
        valores.append(num)
    if num == "":
        break
valores.sort()
print(valores)