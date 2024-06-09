def cabeçalho(txt):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)
def arquivoExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criacao do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabeçalho('Pessoas cadastradas')

        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:<3}anos')
    finally:
        a.close()

def cadastrar(arq,nome='desconhecido', idade = 0):
    try:
        a=open(arq, 'at')
    except:
        print('houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registo de {nome} adicionado')
            a.close()