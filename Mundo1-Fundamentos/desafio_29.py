vl = float(input('Digite a velocidade atual do carro: '))

if vl > 80:
    multa = (vl-80) * 7
    print(f'Você ultrapassou a velocidade permitida de 80km/h, você foi multado com valor de R${multa:.2f}')
else:
    print('Você não ultrapassou a velocidade permitida, parabéns!!!')