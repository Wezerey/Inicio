from datetime import datetime
dados= dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Data Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira e trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contrato'] = int(input('Ano de contrato:'))
    dados['salario'] = float(input('Salario:'))
    dados['aposentadoria'] = (dados['contrato'] + 35) - datetime.now().year
print('='*30)
for k,v in dados.items():
    print(f' -   {k} Tem o valor {v}')