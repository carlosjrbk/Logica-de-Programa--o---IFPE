valores = []
while True:
    num = int(input("Digite um numero inteiro: "))
    if num not in valores:
        valores.append(num)
    if num == 0:
        valores.sort(reverse=True)
        break
for i in valores:
    print(i)