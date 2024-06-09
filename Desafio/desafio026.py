nome=input('Digite seu nome: ')
print('Em que posicao fica a primeira letra A:{}'.format(nome.find('a')))
print('Em que posicao fica a ultima letra A:{}'.format(nome.rfind('a')))
print('Quantas vezes aparece A na frase:{}'.format(nome.count('a')))