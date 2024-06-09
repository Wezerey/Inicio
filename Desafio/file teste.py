lista_existente = [1, 2, 3]
novo_valor = int(input(''))

# Usando o método append() para adicionar um único valor
lista_existente.append(novo_valor)
print(lista_existente)

# Usando o método extend() para adicionar múltiplos valores
valores_a_adicionar = [5, 6, 7]
lista_existente.extend(valores_a_adicionar)
print(lista_existente)
