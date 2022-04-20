#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
#vd = valor do desconto
n = float(input('Digite o preço atual do produto: '))

vd = n*0.05
total= n-vd

print(f'O novo valor do produto é de R${total:,.2f} reais')