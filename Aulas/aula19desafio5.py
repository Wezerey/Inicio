galera = list ()
pessoa = dict ()
media = soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('Sexo : [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade']=int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! responda apenas S ou N')
    if resp == 'S':
        break
print('*-'*30)
print(f'A) Ao todo temos {len(galera)}')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print('C) as mulheres cadastradas foram',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) lista das pessoas que esta oacima da media: ',end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k,v in p.items():
            print(f'{k} = {v}: ',end='')
        print()
print('Encerrado>>>>>>>>>>>>>>>>>')