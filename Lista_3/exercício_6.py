ptm = 3
i = 0
seq = 2
termo = 0
print(ptm)

while i < 14:
    if i == 0:
        termo = ptm + 4 / (seq * (seq + 1) * (seq + 2))
        seq += 2
        print(termo)
        i += 1
    termo = termo - 4 / (seq * (seq + 1) * (seq + 2))
    seq += 2    
    print(termo)
    i += 1