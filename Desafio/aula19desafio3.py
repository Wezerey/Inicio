from datetime import datetime
dados = dict()
dados['nome']=str(input('Nome: '))
nas=int(input('Ano de nascimento'))
dados['idade'] = datetime.now().year - nas
dados['ctps'] = int(input('Carteira de trabalho(0 nao tem):'))
if dados['ctps'] != 0:
    dados['contratacao']=int(input('Ano de contratacao: '))
    dados['salario']=float(input('Salario: R$'))
    dados['aposentadoria']=dados['idade']+((dados['contratacao']+35)-datetime.now().year)
print(dados)