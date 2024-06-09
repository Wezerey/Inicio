contador_idade = contador_home = contador_mule =0
while True:
    print('='*30)
    print('     Cadastre uma pessoa   ')
    print('='*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/H] ')).upper().strip()
    print('='*30)
    if idade >= 18:
        contador_idade += 1
    elif sexo == 'H':
        contador_home += 1
    elif sexo == 'M' and idade <= 20:
        contador_mule += 1
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()
    print('='*30)
    if resposta == 'N':
        break
print(f'Total de pessoa com mais de 18 anos: {contador_idade}')
print(f'Total de homens: {contador_home}')
print(f'Total de mulhers com menos de 20 anos {contador_mule}')

