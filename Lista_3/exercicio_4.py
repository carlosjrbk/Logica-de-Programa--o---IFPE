n=1
tl = 0
ns=" "
media=0
al = 13
print('letra ----- nota \n A+ ------ 4.0 \n A- ------ 3.7 \n B+ ------ 3.3 \n B- ------ 2.7 \n C+ ------ 2.3 \n C- ------ 1.7 \n D+ ------ 1.3 \n D- ----- 0')
print('DE ACORDO COM A TABELA')
print('')
while n <= 8:
    nt = input(f"INSIRA A {n}° LETRA COM SINAL PARA CALCULAR A MEDIA DA TURMA :  ").upper().strip()
    ns += nt
    n +=1
    if nt == "A+":
        tl += 4.0
    if nt == "A-":
        tl +=3.7
    if nt == "B+":
        tl+= 3.3
    if nt == "B-":
        tl += 2.7
    if nt == "C+":
        tl +=2.3
    if nt == "C-":
        tl +=1.7
    if nt == "D+":
        tl += 1.3
    if nt == "D-":
        tl += 0
media = tl / 8
print('')
print (f"AS NOTAS FORAM: {ns} ")
print('')
print(f"O TOTAL DE PONTOS DA TURMA É: {tl:.2f}")
print('')
print(f"A MEDIA DA TURMA PARA OS {al} ALUNOS É : {media:.2f}")