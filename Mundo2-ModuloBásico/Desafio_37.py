n = int(input('Digite um numero inteiro qualquer: '))

print('------[1] para binário------------')
print('------[2] para octal------------')
print('------[3] para hexagono------------')

c = int(input('Escolha uma base de conversão: '))


if c == 1:
    n = format(n, "b")
    print(f'binario: {n}')

elif c == 2:
    n = format(n, "o")
    print(f'octal: {n}')

elif c == 3:
    n = format(n, "x")
    print(f'hexagonal: {n}')


