matriz = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]
for l in range(0, 10):
    for c in range(0, 2):
        matriz[l] [c] = float(input(f"Digite um valor para [{l}, {c}:]"))
        print('-+'*30)
for l in range(0, 10):
    for c in range(0, 2):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()