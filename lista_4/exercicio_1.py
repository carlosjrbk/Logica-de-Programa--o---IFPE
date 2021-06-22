t = 0
x = 1
for cont in range(1,16):
    idade = int(input(f"{x} informe sua idade: "))
    x += 1
    if idade >= 18:
        t += 1
print(f"A quantidade de pessoas com idade maior ou igual a 18 é de: {t}" )
    