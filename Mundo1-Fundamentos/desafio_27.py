nome = str(input('Digite um nome completo: ')).strip()
n = nome.split()

print(f'Primeiro: {n[0]}')
print(f'Ultimo: {n[len(n)-1]}')