#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

n = float(input('Digite um valor em m^2: '))
c = n*100
mm = n*1000
dm = n*10
dam = n/10
hm = n/100
km = n/1000
#print(f'O valor {n} m^2 convertido é {c}cm e {mm}mm')
print(f'o valor de {n}m^2 convertido é {c:.0f}cm e {mm:.0f}mm, {dm:.0f}dm, {dam:.0f}dam, {hm}hm,{km}km')
