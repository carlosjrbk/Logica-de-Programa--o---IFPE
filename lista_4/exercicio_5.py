x = n1 = n2 = n3 = 0
for cont in range(1, 6):
    x += 1
    resp = int(input (f"QUANTAS VEZES O {x}° ALUNO UTILIZOU O RESTAURANTE NO ULTIMO MÊS: "))
    print()
    if resp == 0:
        break
    elif (resp < 10):
        n1 += 1  
    elif (resp >= 10) and  (resp < 16):
        n2 += 1
    elif resp > 15:
        n3 += 1
    elif x == 5:
        break
t = n1 + n2 + n3
p1 = (n1*100) / t
p2 = (n2*100) / t
p3 = (n3*100) / t

print (f"PERCENTUAL QUE UTILIZARAM MENOS DE 10 VEZES: {p1:.2f}""%" )
print (f"PERCENTUAL QUE UTILIZARAM ENTRE 10 e 15 VEZES: {p2:.2f}""%" )
print (f"PERCENTUAL QUE UTILIZARAM MAIS DE 15 VEZES: {p3:.2f}""%" )