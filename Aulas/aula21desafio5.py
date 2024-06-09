def notas(*num,sit=False):
    """
    >> funcao para nalisar notas e situacao de varios alunos
    :param num:uma ou mais nota dos alunos
    :param sit:Valor opcional para indicar se a situacao é boa ou ruim
    :return:Dicionarios com varias informacoes.
    """
    r = dict ()
    r['total']= len(num)
    r['maior']= max(num)
    r['menor']= min(num)
    r['media']= sum(num) / len(num)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'BOA'
        elif r['media'] >= 5:
            r['situaçao'] = 'RAZOAVEL'
        else:
            r['situaçao'] = 'RUIM'
    return r



res=notas(5.5,2.5,10,6.5,sit=True)
print(res)
help(notas)