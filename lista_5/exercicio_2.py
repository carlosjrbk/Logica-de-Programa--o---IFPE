valores = []
for i in range(1, 11):
    num = int(input("Digite um numero inteiro: "))
    if num not in valores:
        valores.append(num)
valores.sort()
print(valores)
