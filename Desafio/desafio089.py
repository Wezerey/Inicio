Alunos_Medias = []
r = ''
n = 0
while r != 'n':
    nome = str(input('Nome: '))
    nota1 = float(input('nota: '))
    nota2 = float(input('nota: '))
    media = (nota1 + nota2) / 2
    Alunos_Medias.append([nome,[nota1,nota2],media])
    r = str(input('Quer continuar? [S/N] ')).lower().strip()
print(Alunos_Medias)
print(f'No. NOME           MEDIA')
print('-'*30)
for x in range(0,len(Alunos_Medias)):
    print(f'{x}   {Alunos_Medias[x][0]:15}{Alunos_Medias[x][2]}')
print('-'*30)
n = int(input('Mostrar notas de qual aluno? (999 Interrompe) '))
while n != 999:
    if n < (len(Alunos_Medias)):
        print(f'Notas de {Alunos_Medias[n][0]} sao {Alunos_Medias[n][1]}')
        n = int(input('Mostrar notas de qual aluno? (999 Interrompe) '))
    else:
        n = int(input('Tente novamente... Mostrar notas de qual aluno? (999 Interrompe) '))