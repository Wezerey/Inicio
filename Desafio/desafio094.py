cadastro = dict()
galera = list()
mulheres = list()
MaiorIdade = list()
r = ''
Soma = media = 0

while r != 'n':
    cadastro['Nome']=str(input('Nome:'))
    cadastro['Sexo'] = str(input('Sexo:'))
    cadastro['Idade'] = int(input('Idade:'))
    galera.append(cadastro.copy())
    if cadastro['Sexo'] == 'f':
        mulheres.append(cadastro['Nome'])
    r = str(input('Deseja continuar [S/N]? '))
for x in galera:
    Soma += x['Idade']
media = Soma /2
print(f'ao total foram cadastrados {len(galera)} pessoas')
print(f'a media de idade é de {media}')
print(f'as mulheres cadastradas sao:',end='')
for x in mulheres:
    print(x,end=' ')
print('')
for x in galera:
    if x['Idade'] > media:
        for k,v in x.items():
            print(f'{k} = {v}',end=';')
print()