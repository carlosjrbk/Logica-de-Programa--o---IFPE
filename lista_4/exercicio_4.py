chico = 1.50
ze = 1.10
ano = 0
for cont in range(0,100):
    if chico > ze:
        chico += 0.02
        ze += 0.03
        ano += 1
print('será necessario' , ano, 'anos')
        
