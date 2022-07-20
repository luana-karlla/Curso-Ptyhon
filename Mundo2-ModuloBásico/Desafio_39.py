anoNasc = int(input('Digite o ano do seu nascimento: '))

idade = (2022-anoNasc)

if idade < 18:
    print(f'Ele ainda vai se alistar, ele tem {idade} anos de idade')
elif idade == 18:
    print(f'Você ja está na hora de se alistar, voce tem {idade} anos')
elif idade > 18:
    print(f'Voce passou do tempo de se alistar, voce tem {idade} anos')