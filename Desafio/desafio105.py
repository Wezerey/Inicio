def notas(*num,sit=False):
    """
    >> funcao para nalisar notas e situacao de varios alunos
    :param num:uma ou mais nota dos alunos
    :param sit:Valor opcional para indicar se a situacao é boa ou ruim
    :return:Dicionarios com varias informacoes.
    """
    dicio = dict ()
    dicio.clear()
    dicio['total']=len(num)
    maior = menor = num[0]
    media = 0
    for q in num:
        media += q
        if q > maior:
            maior = q
        elif q < menor:
            menor = q
    dicio['maior'] = maior
    dicio['menor'] = menor
    dicio['media'] = media/len(num)
    if sit:
        if dicio['media'] >= 6:
            dicio['situaçao'] = 'BOA'
        else:
            dicio['situaçao'] = 'RUIM'
    return dicio


res=notas(5.5,2.5,10,6.5,sit=True)
print(res)
help(notas)
