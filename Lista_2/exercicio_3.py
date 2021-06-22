mes = input('DIGITE O MES COM A PRIMEIRA LETRA MAIÚSCULA: ')

if mes == "Janeiro" or mes == "Março" or mes == "Maio" or mes =='Agosto' or mes == 'Outubro' or mes == 'Dezembro':
     print(f'{mes} tem 31 dias')
elif mes == 'Fevereiro':
    print(f'{mes} tem 28 ou 29 dias')
elif mes == 'Abril' or mes == 'Junho' or mes == 'Setembro' or mes == 'Novembro':
    print(f'{mes} tem 30 dias')
else:
    print('ERRO MES DIGITADO  INCORRETAMENTE')