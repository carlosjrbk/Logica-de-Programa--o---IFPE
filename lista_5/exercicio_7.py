z = list()
x = 1
maior6 = 0
menor6 = 0
al = 1
while x <=10:
    n1 = float(input(f'Informe a Primeira Nota do Aluno {al} : '))
    n2 = float(input(f'Informe a Segunda Nota do Aluno {al} : '))
    al+=1
    print("-"*20)
    media = (n1 + n2) / 2
    z.append([[n1, n2, media]])
    x+=1
print(f" {'Alunos':<4} {'Notas':>10} {'Média':>8} ")
print('-'*40)
h=1
for i,a in enumerate(z):
    print(f"Aluno {h:<4} {a[0]}")
    if a[0][2]>=6:
        maior6+=1
    else:
        menor6+=1
h+=1
print(f"ALUNOS COM A MEDIA ABAIXO DE 6: {menor6}" )
print(f"ALUNOS COM NOTA MAIOR OU IGUAL 6: {maior6}")