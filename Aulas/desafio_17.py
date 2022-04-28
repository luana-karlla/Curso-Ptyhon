import math

cOposto = float(input('Digite um numero para Cateto Oposto: '))
cAdjacente = float(input('Digite um numero para Cateto Adjacente: '))

print(f'O comprimento da hipotenusa é:{math.hypot(cOposto, cAdjacente):.2f}')