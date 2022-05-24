salario = float(input('Digite o valor do salário: '))

if salario >= 1250:
    #calcular o aumento 10%
    #salario = (salario * (10 / 100)) + salario
    valorAumento = salario * (10/100) #calculo do valor do aumento
    salario = salario + valorAumento
    print(f'O valor do aumento foi de R${valorAumento:.2f} e o salário atualizado é de R${salario:.2f}')

else:
    # calcular o aumento 15%
    valorAumento = salario * (15/100)
    salario = salario + valorAumento
    print(f'O salario sofreu um aumento R${valorAumento:.2f} e o salário atualizado é de R${salario:.2f}')

