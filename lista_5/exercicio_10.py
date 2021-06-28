nomes = []
valores = []
cont = 0

for l in range(5):
  linha = []
  produto = input(f'Digite o nome do produto {cont + 1}: [Se o nome for maior que 10 caracteres, favor abreviar.] ').upper()
  while len(produto) > 10:
    print("Você digitou mais de 10 caracteres, por gentileza considerar este limite e abreviar o nome do produto.")
    print("")
    produto = input(f'Digite o nome do produto {cont + 1}: [Se o nome for maior que 10 caracteres, favor abreviar.] ').upper()
  nomes.append(produto)
  compra = float(input(f'Digite o valor de compra do produto {produto}: R$').replace(",","."))
  linha.append(compra)
  venda = float(input(f'Digite o valor de venda do produto {produto}: R$').replace(",","."))
  linha.append(venda)
  valores.append(linha)
  cont = cont + 1
  print("")

for produto in range(0, 10):
  busca = input("Digite o nome do produto para visualizar o lucro: ").upper()
  indiceProduto = nomes.index(busca)
  lucro = valores[indiceProduto][1] - valores[indiceProduto][0]
  print("")
  print("O lucro obtido com a venda deste produto foi de: R${:.2f}".format(lucro))
  print("")
  pergunta = input("Precisa visualizar o lucro de outro produto?: [S | N]")
  if pergunta != "S":
    break