distancia = float(input('Qual a distancia da viagem? '))

if distancia <= 200:
    precoP = distancia * 0.50
    print(f'O preço da passagem de {distancia}km/h é de R${precoP}')

elif distancia > 200:
    precoP = distancia * 0.45
    print(f'O preço da passagem de {distancia}km/h é de R${precoP}')

