n = int(input('Digite um numero de 0 a 9999: '))

print(f'Unidade: {str(n%10)[0]}')
print(f'Dezena: {str(n%100)[0]}')
print(f'Centena: {str(n%1000)[0]}')
print(f'Milhar: {str(n%10000)[0]}')



