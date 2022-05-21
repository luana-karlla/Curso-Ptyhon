import random
from time import sleep

numero = int(input('Digite um numero entre 0 e 5...tente adivinhar...: '))

print('PROCESSANDO...')
sleep(3)

n2 = random.randint(0, 5)

if numero == n2:
    print(f'Parabéns, você conseguiu me vencer!!! O número escolhido foi: {n2}')

elif numero >=6 or numero <=-1:
    print('Numero não compatível com o descrito, tente novamente!!!')

else:
    print(f'Errou!!! Cuen Cuen Cuen Cuennnn!!! O número escolhido foi: {n2}')




