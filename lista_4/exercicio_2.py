for cont in range (1,16):
    nome = input("Informe seu nome: ")
    valor = float(input("Informe o valor da Compra: "))
    if valor < 1000:
        total = valor - (valor * 0.1)
        print( nome + " " "pagará " + str(total) + " por ter comprado a baixo de R$1000,00")
    else:
        valor > 1000
        total = valor - (valor * 0.15)
        print( nome + " " "pagará " + str(total) + " por ter comprado a acima de R$1000,00")
        