aluno = dict ()
aluno['nome'] = str(input('Nome:'))
aluno['media'] = float(input(f'Media de {aluno['nome']}:'))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperacao'
else:
    aluno['situacao'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')