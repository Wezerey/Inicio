aluno=dict()

aluno['nome']=str(input('Nome: '))
aluno['media']=float(input('media: '))

print(f'Nome é igual a {aluno['nome']}')
print(f'Media é igual a {aluno['media']}')
if aluno['media'] >= 7 :
    print('Aluno aprovado')
else:
    print('Aluno reprovado')