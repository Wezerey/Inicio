galera = list ()
dado = list ()
totMai = totMen = 0
for x in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    print(dado)
print(galera)
for x in galera:
    if x[1] >= 18:
        print(f'{x[0]} é maior de idade')
        totMai += 1
    else:
        print(f'{x[0]} é menor de idade')
        totMen += 1
print(f'temos {totMen} menor de idade e temos {totMai} maior de idade')