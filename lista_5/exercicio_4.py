listaCarro = [['Vectra', 9], ['Gol', 10], ['Corsa', 11], ['Fit', 12.5]]
precoGasolina = 4.69
distancia = 1000
print('Custo de Comb. --------------------------veiculo')
print("-"*45)
for v in listaCarro:
    consumo = 1000 / v[1]
    Custo = consumo * precoGasolina
    print(f'{Custo:.2f}-----------------------------------', v[0])
if v[1] > len(listaCarro):
  print('Modelo mais economico-->', v[0])