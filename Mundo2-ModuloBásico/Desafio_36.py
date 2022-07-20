#Calculo de financiamento bancario para compra de imóvel

vlCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anosPagar = float(input('Em quantos anos você irá pagar?: '))

prestacao = vlCasa/(anosPagar*12)
vMinimo = salario * 0.3

print(f'O valor da casa R${vlCasa} reais pagae em {anosPagar} anos ficara no valor de R${prestacao}')

if prestacao <= vMinimo:
    print(f'Empréstimo Aprovado!')
else:
  print(f'Empréstimo Negado!')