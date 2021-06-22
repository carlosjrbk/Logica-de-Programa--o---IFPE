n = int(input("INSIRA O NUMERO DE TERMOS DA PA: "))
pt = int(input("INSIRA O 1° TERMO DA PA: "))
r = int(input("INSIRA A RAZÃO DA PA: "))
print("*"*40)
print("OS TERMOS DA PA SÃO")
calc = pt + ( n - 1 )*r
for i in range(pt, calc+r, r):
    print(f'{i}',end='->')
soma = n * (pt + calc) // 2
print()
print(">A SOMA DOS TERMOS DA PA É:->",soma)