import random

numero = int(input('Digite um numero entre 0 e 5: '))

n2 = random.randint(0, 5)

if numero == n2:
    print(f'Parabéns, você acertou!!! O número escolhido foi: {n2}')

elif numero >=6 or numero <=-1:
    print('Numero não compátivel com o descrito, tente novamente!!!')

else:
    print(f'Errou!!! Tente Novamente!!! O número escolhido foi: {n2}')


"""if numero >=6:
    print('Numero fora da régua, tente novamente!')"""



