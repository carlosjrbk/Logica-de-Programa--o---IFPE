dia = int(input('INFORME O DIA DO MES: '))
mes = str(input('INFORME O MES EM LETRAS MINUSCULAS: '))

if mes in ('janeiro'):
    print('VERÃO')
elif mes == 'fevereiro' and (dia > 28):
    print('ERRO DATA INCORRETA EM FEVEREIRO')
elif mes == 'fevereiro':
    print('VERÃO')
elif mes == 'março' and (dia >= 20):
    print('OUTONO')
elif mes == 'março' and (dia < 20):
    print('VERÃO')  
elif mes in ('abril', 'maio'):
    print('OUTONO')
elif mes == 'junho' and (dia >= 21):
    print('INVERNO')
elif mes == 'junho'and (dia < 21):
    print('OUTONO')
elif mes in ('julho','agosto'):
    print('INVERNO')
elif mes == 'setembro' and (dia >= 22):
    print('PRIMAVERA')
elif mes == 'setembro' and (dia < 22):
    print('INVERNO')    
elif mes in ('outubro','novembror'):
    print('PRIMAVERA')
elif mes == 'dezembro' and (dia >= 21):
    print('VERÃO')
elif mes == 'dezembro' and (dia < 20):
    print('PRIMAVERA')
else:
    print('INFORMAÇÃO INCORRETA')



