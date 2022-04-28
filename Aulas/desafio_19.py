import random

n1 = str(input('Digite o nome do aluno n°1: '))
n2 = str(input('Digite o nome do aluno n°2: '))
n3 = str(input('Digite o nome do aluno n°3: '))
n4 = str(input('Digite o nome do aluno n°4: '))

lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)

print(f'O aluno escolhido apagar o quadro foi: {sorteio}')