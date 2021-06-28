valores = []
while True:
    num = input("Digite um numero inteiro: ")
    valores.append(num)
    if num == " ":
        valores.sort()
        break
print(valores[::-1])

