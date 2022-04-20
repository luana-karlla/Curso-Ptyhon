#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
#va = valor do aumento

n = float(input('Digite o salario do funcionario: '))

va = n * 0.15
total = n + va

print(f'O novo salario do funcionario é R${total:,.2f}')