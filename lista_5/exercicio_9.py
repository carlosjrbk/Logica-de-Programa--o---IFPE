gab = ["A", "C", "E", "B", "D", "B", "B", "C", "A", "E"]
n = []
while True:
    p = []
    print('-'*50)
    nome = input('NOME DO CANDIDATO(digite N para sair): ').upper()
    if nome == "N":
        break
    else:
        ac = 0
        p.append(nome)
        for i in range(1, 11):
            print('-'*50)
            resposta = input('INFORME A RESPOSTA ENTRE - A e E: ').upper()
            if resposta == gab[i-1]:
                ac += 1
            p.append(resposta)
        p.append(ac)
        n.append(p)
for i in range(0, len(n)):
    print('NOTA FINAL->',n[i][0], ": ", n[i][11])
