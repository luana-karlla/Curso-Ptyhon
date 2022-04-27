import math

cOposto = float(input('Digite um numero para Cateto Oposto: '))
cAdjacente = float(input('Digite um numero para Cateto Adjacente: '))

print(f'O comprimento é: ', math.hypot(cOposto, cAdjacente))