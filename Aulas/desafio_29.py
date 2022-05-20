vl = float(input('Digite a velocidade do carro: '))

if vl > 80:
    multa = (7*10) + vl
    print(f'Você ultrapassou a velocidade permitida de 80km/h, sua multa foi de R${multa}')
else:
    print('Você não ultrapassou a velocidade permitida, parabéns!!!')