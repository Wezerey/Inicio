r = ''
pessoas = []
totalpessoas = []
pp = []
pl = []
while r != 'n':
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    r=str(input('Quer continuar? [S/N] ')).lower().strip()
    totalpessoas.append(pessoas[:])
    pessoas.clear()
for x in totalpessoas:
    if x[1]>=100:
        pp.append(x[0])
    elif x[1]<=70:
        pl.append(x[0])
print(f'Ao todo foi cadastradas {len(totalpessoas)} pessoas')
print(f'As pessoas que estao abaixo de 70 kg sao {pl}')
print(f'As pessoas que estao abaixo de 100 kg sao {pp}')
