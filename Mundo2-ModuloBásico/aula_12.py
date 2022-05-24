nome = str(input('\033[1;35m Qual é o seu nome?: '))
if nome == '\033[1;35m Luana \033[m':
    print(f'\033[1;32m;40 Que lindo nome voce, {nome}')
elif nome == 'Joao' or nome == 'Pedro' or nome == 'Julia':
    print('\033[31;40m Seu nome é bem popular no Brasil \033[m')
elif nome in 'Anna Sandra Maria':
    print('\033[4;31;44m Belo nome feminino \033[m')
    
print(f'\033[31;40m Tenha um bom dia, {nome} \033[m')
