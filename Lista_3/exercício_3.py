pr_in = 0
pr_desc = 0
tb=[]
pd = " "
while True:
    pd = str(input("DIGITE O NOME DO PRODUTO: "))
    pr_in = float(input("DIGITE O PREÇO DO PRODUTO R$ ").replace("," , "."))
    pr_desc = pr_in - (pr_in * 0.6)
    tb.append([pd, pr_in, pr_desc])
    resp = " "
    while resp not in 'SN':
        resp = str(input("QUER CONTINUAR A PESQUISA DE PREÇO? [S/N] ")).strip().upper() [0]
    if resp == 'N':
        break
print('RESULTADO DA PESQUISA DE PREÇO ')
for t in tb:
    print(f"NOME DO PRODUTO --- {t[0]} --- PREÇO INICIAL é: {t[1]:.2f} --- VALOR DO PRODUTO COM DESCONTO DE 60% é: {t[2]:.2f}")