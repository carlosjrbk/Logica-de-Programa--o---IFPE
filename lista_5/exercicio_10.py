n = []
v = []
cont = 0

for l in range(5):
  l = []
  pr = input(f'NOME DO PRODUTO? {cont + 1}: [maior que 10 caracteres, abreviar.] ').upper()
  while len(pr) > 10:
    print("ERRO!! MAIS DE DEZ CARACTERES DIGITADOS.")
    print("")
    pr = input(f'NOME DO PRODUTO? {cont + 1}: [maior que 10 caracteres, abreviar.] ').upper()
  n.append(pr)
  compra = float(input(f'VALOR DO PRODUTO? {pr}: R$').replace(",","."))
  l.append(compra)
  ve = float(input(f'VALOR DE VENDA DO PRODUTO? {pr}: R$').replace(",","."))
  l.append(ve)
  v.append(l)
  cont = cont + 1
  print("")

for pr in range(0, 10):
  busca = input("NOME DO PRODUTO PARA VIZUALIZAR O LUCRO: ").upper()
  indiceProduto = n.index(busca)
  lucro = v[indiceProduto][1] - v[indiceProduto][0]
  print("")
  print("O LUCRO COM O PRODUTO FOI DE: R${:.2f}".format(lucro))
  print("")
  pergunta = input("QUER VER O LUCRO DE OUTRO PRODUTO?: [S | N]").upper()
  if pergunta != "S":
    break