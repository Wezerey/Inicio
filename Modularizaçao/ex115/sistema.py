from lib.interface import *
from lib.arquivo import *

arq = 'Cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade=leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('Erro, opcao invalida')

