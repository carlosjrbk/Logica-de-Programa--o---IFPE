z = list()
x=1
al=1
while x <= 10:
    n1 = float(input(f'PRIMEIRA NOTA DO ALUNO {al} : '))
    n2 = float(input(f'SEGUNDA NOTA DO ALUNO {al} : '))
    al += 1
    print("-"*20)
    media = (n1 + n2) / 2
    z.append([[n1, n2, media]])
    x += 1
    print(f" {'Nº':<4} {'Notas':>10} {'Média':>10} ")
    print('-'*40)
    h = 1
for i, a in enumerate(z):
    print(f"Aluno {h:<4} {a[0]}")
    h += 1
