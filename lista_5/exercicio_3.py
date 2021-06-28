from random import randint
sorteio = []
i = 0
while True:
    n = randint(1, 60)
    if n not in sorteio:
        sorteio.append(n)
        i += 1
    if i >= 6:
        break
sorteio.sort()
print(f"Os numeros sorteados foram {sorteio}")