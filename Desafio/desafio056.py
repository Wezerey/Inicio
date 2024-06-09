nomemaior = ''
maior = 0
somaidade = 0
mulher = 0
for x in range(1, 5):
    nome=str(input('Nome: ')).capitalize().strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo: ')).capitalize().strip()
    somaidade += idade
    media = somaidade / 4
    if x == 1 :
        maior = idade
        nomemaior = nome
    elif idade > maior and sexo == 'H':
        maior = idade
        nomemaior = nome
    elif idade < 20 and sexo == 'M':
            mulher += 1

print(f'A media de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maior} anos e se chama {nomemaior}')
print(f'Ao todo temos {mulher} mulhers menores de 20 anos')

