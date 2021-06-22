n1 = n2 = n3 = 0
print('PARA ENCERRAR A PEQUISA E MOSTRAR O RESULTADO DIGITE -> [0]')
print('')
while True:
    resp = int(input ("QUANTAS VEZES VOCÊ UTILIZOU O RESTAURANTE NO ULTIMO MÊS: "))
    if resp == 0:
        break
    elif (resp <= 10):
        n1 += 1  
    elif (resp > 10) and  (resp < 16):
        n2 += 1
    elif resp > 15:
        n3 += 1
    
t = n1 + n2 + n3
p1 = (n1*100) / t
p2 = (n2*100) / t
p3 = (n3*100) / t

print (f"PERCENTUAL QUE UTILIZARAM MENOS DE 10 VEZES: {p1:.2f}""%" )
print (f"PERCENTUAL QUE UTILIZARAM ENTRE 10 e 15 VEZES: {p2:.2f}""%" )
print (f"PERCENTUAL QUE UTILIZARAM MAIS DE 15 VEZES: {p3:.2f}""%" )