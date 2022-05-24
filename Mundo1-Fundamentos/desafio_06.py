#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('\033[4;35mDigite um número:\033[m'))
d = n*2
t = n*3
r = n**(1/2)
print(f'\033[1;30;44mO dobro de {n}, é {d}, o triplo é {t} e a raiz quadrada é {r}\033[m')