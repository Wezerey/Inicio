nome = str(input('Qual seu nome ? ')).lower()
if nome == 'weslley':
    print('Que nome bonito')
elif nome == 'paulo' or nome == 'joao':
    print('seu nome é bem popular')
elif nome in 'ana kay':
    print('que nome feminino bonito')
print(f'tenha um bom dia {nome.capitalize()}')