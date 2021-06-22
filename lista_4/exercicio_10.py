
for i in range(0, 11):
    print("*******SUPERMERCADO BALAIO*********")
    n = 1
    tot = 0
    for i in range(1, 11):
        pr = float(input("INFORME O VALOR DO PRODUTO {}: R$ ".format(n)))
        n += 1
        tot += pr
        if pr == 0:
            break
    print("-"*30)
    print("TOTAL DA COMPRA: R$ {:.2f} ".format(tot))
    d = float(input("DINHEIRO RECEBIDO: R$ "))
    print("TROCO: R$ {:.2f}".format(d - tot))
    print("-"*30)
    r = input(" 0 PARA REINICIAR / 1 ENCERRAR: ")
    if r == "0":
        continue
    else:
        print("CAIXA FECHADO...")
        break