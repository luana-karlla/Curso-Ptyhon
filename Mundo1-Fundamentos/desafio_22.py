nome = str(input('Digite um nome: '))
divido = nome.split()

print(f' O nome em MAIUSCULA é: {nome.upper()}')
print(f' O nome em minuscula: {nome.lower()}')
#len(''.join(nome.split())
print('Total de letras sem considerar os espaços são de', len(''.join(nome.split())))
print('O Primeiro nome tem', len(''.join(divido[0])), 'letras')



