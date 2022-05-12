nome = str(input('Digite o nome de uma pessoa: ')).strip()
print(f'Seu nome tem Silva? {"silva" in nome.lower().split()}')
