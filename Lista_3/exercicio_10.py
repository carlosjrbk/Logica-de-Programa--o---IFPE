tm = 1
while tm <= 5:
    totalTm = 0
    qt = int(input(f"Quantos alunos você possui na turma {tm}? "))
    contTm1 = 1
    ntotal = 0
    while contTm1 <= qt:
        n = input("Digite o nome do aluno: ").capitalize()
        ntaAl = input("Digite a nota do aluno: ")
        ntaAl = float(ntaAl.replace(",","."))
        ntotal = ntotal + ntaAl
        mNotasT1 =  ntotal/qt
        contTm1 += 1
    print("")
    print(f"A MÉDIA DA TURMA {tm} é: {mNotasT1}")
    print("-" * 25)
    tm = tm + 1
