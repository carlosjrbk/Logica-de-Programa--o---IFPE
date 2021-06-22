x = 1
quant = maior = menor = soma = 0
emp = int(input('INFORME A QUANTIDADE DE FUNCIONARIOS: '))
print('')
while x <= emp:
    f = str(input('INFORME O NOME DO FUNCIONARIO - %d: '%x))
    x = int(x)
    sl = float(input('INFORME O SALARIO DO FUNCIONARIO - %d: ' %x))
    print('')
    soma = soma + sl
    x += 1
    quant += 1
    if quant == 1:
        maior = menor = sl
    else:
        if sl > maior:
            maior = sl
        if sl < menor:
            menor = sl
print(f'O MAIOR salario digitado foi {maior}')
print(f'O MENOR salario digitado foi {menor}')
print('')          
print("A média salarial é: %1.2f" % (soma/emp))