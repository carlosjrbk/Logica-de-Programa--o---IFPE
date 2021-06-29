ms = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temp = []

for m in range(0, len(ms)):
    temp.append(float(input("Digite a temperatura do mes de " + ms[m] + ": ")))

mAnual = sum(temp)/len(temp)
print('-'*45)
print(f'Temperatura média anual: {mAnual}')
print('-'*45)
print('Meses Com a Temperatura acima da media')
print("-"*45)
for m in range(0, len(temp)):
    if temp[m] > mAnual:
        
        print (str(m+1) + " - " + ms[m])         