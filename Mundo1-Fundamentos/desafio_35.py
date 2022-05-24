ab = float(input('Digite o seguimento da primeira reta: '))
cd = float(input('Digite o seguimento da segunda reta: '))
ef = float(input('Digite o seguimento da terceira reta: '))

if ab < cd + ef and cd < ab + ef and ef < ab + cd:
    print(f'formam um triangulo retangulo')

else:
    print(f'não formam um triangulo retangulo')