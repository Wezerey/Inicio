nome=str(input('Digite uma frase: ')).lower().strip()
print('Em que posicao fica a primeira letra A:{}'.format(nome.find('a')+1))
print('Em que posicao fica a ultima letra A:{}'.format(nome.rfind('a')+1))
print('Quantas vezes aparece A na frase:{}'.format(nome.count('a')))