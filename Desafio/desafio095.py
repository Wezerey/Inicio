lista = list()
dicionario = dict()
gols = list()
contador = 0
while True:
    dicionario['nome']=str(input('Nome:'))
    dicionario['partidas']=int(input(f'Quantas partidas {dicionario['nome']} jogou? '))
    gols.clear()
    for x in range(dicionario['partidas']):
        gols.append(int(input(f'Quantos gols na partida {x+1}: ')))
    dicionario['gols']= gols[:]
    dicionario['total']=sum(gols)
    lista.append(dicionario.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break
print('-'*50)
print('cod nome           gols            total')
print('-'*50)
for x in lista:
    print(f'{contador:3} {x["nome"]:15}{str(x['gols']):15} {x["total"]} ')
    contador+=1
print('-'*50)
print(lista)
while True:
    dados=int(input('Mostrar dados de qual jogador? (999 parar)'))
    if dados != 999:
        if dados > (len(lista)-1):
            print(f'ERRO! Jogador nao existe com codigo {dados}!')
        else:
            print(f' -- LEVANTAMENTO DO JOGADOR {lista[dados]['nome']}:')
            for x in range (len(lista[dados]['gols'])):
                print(F'      na partida {x+1}, fez {dicionario["gols"][x]} gols')
        print('-' * 50)
    else:
        break
print('VOLTE SEMPRE!!')