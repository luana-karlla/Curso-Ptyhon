#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

n = float(input('Digite um valor em m^2: '))
c = n/100
mm = n/1000

print(f'O valor {n} m^2 convertido em cm é {c} e em mm é {mm}')
