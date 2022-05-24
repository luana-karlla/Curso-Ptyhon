frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A apareceu {frase.count("A")} vezes')
print(f'A letra A apareceu na posicao: {frase.find("A")+1}')
print((f'A ultima letra A apareceu na posicao: {frase.rfind("A")+1}'))



