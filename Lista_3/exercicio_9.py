x = int(input('QUAL A PRIMEIRA TABUADA?: '))
y = int(input('QUAL A ULTIMA TABUADA?: '))
while x <= y:
  cont = 0
  print(f'\nTABUADA DE: {x}')
  while cont <= 10:
    print(f'{x} x {cont} = {x*cont}')
    cont += 1
  x += 1