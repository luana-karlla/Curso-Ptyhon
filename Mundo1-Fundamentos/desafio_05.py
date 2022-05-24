#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('\033[32mDigite um número: \033[m'))
ant = n-1
suc = n+1
print(f'\033[43mO antecessor de {n}, é {ant} e o sucessor é {suc}\033[m')