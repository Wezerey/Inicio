from datetime import date
Dicionario = dict()
Dicionario['nome']=str(input('Nome:'))
ano=int(input('Ano de nascimento:'))
Dicionario['idade'] = date.today().year - ano
Dicionario['ctps']=str(input('Numero da carteira de trabalho(se for 0 nao tem):'))
if Dicionario['ctps'] != '0':
    Dicionario['contrato']=int(input('Ano de contrato:'))
    Dicionario['salario']=float(input('Salario:'))
    Dicionario['aposentadoria'] = (Dicionario['contrato'] + 35) - date.today().year
print('='*40)
for k,v in Dicionario.items():
    print(k,'Tem o valor',v)