tupla = (("macaco", 0,), ("galo", 1), ("cão", 2), ("porco", 3), ("rato", 4), ("boi", 5),
         ("tigre", 6), ("Coelho", 7), ("Dragão", 8), ("Serpente", 9), ("Cavalo", 10), ("Carneiro", 11))
print('-'*68)
n = input("PARA SABER SEU SIGNO CHINES DIGITE (sim ou não) PARA SAIR DO PROGRAMA: ")
while n == "sim":
    ano = int(input("INFORME SEU ANO DE NASCIMENTO (AAAA): "))
    sig = ("macaco", "galo", "cão", "porco", "rato", "boi",
                     "tigre", "coelho", "dragão", "Serpente", "Cavalo", "Carneiro")
    sig = sig
    sig = sig[ano % 12]
    print(f'SEU SIGNO CHINÊS É: {sig}')
    n = input('QUER CONTINUAR? (sim ou não): ')
    if n == "não":
       break