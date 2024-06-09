import random
n1=input('Digite o nome do aluno: ')
n2=input('Digite o nome do aluno: ')
n3=input('Digite o nome do aluno: ')
n4=input('Digite o nome do aluno: ')
aluno=[n1,n2,n3,n4]
random.shuffle(aluno)
print('O aluno que vai apagar o Quadro é {}'.format(aluno))