n1 = float(input('Digite um numero inteiro: '))
n2= float(input('Digite outro numero inteiro: '))

if n1 > n2:
    print(f'O primeiro valor é maior.')
elif n1 < n2:
    print(f'O segundo valor é maior.')
elif n1 == n2:
    print(f'Não existe valor maior, os dois sao iguais.')