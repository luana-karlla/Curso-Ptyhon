#Crie um programa  que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere USS1.00 = 3.27

n = float(input('Quanto você tem na carteira em reais?: '))
dolar = n/3.27
print(f'Com R${n}, voce consegue comprar US${dolar:,.2f}')