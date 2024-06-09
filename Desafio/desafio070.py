menor_preco = soma = contador = contador_Menor = 0
menor_nome = ''
print('-'*20)
print('   LOJAS BARATEZA')
print('-'*20)
while True:
    nome_produto = str(input('Informe o produto: '))
    preco_produto = float(input('Informe preco do produto R$:'))
    soma += preco_produto
    contador_Menor += 1
    if preco_produto > 1000:
        contador += 1
    elif contador_Menor == 1:
        menor_preco = preco_produto
        menor_nome = nome_produto
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()
    if resposta == 'N':
        break
print('-'*20)
print(f'O total da compra foi R${soma}')
print(f'Temos {contador} produto com o preco acima de R$1000.00')
print(f'O produto mais barato foi {menor_nome} com o preço de R${menor_preco}')