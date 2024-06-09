def jogador(s,i):
    print(f'O jogador {i} fez {s} gol(s) no campeonato')
nome=str(input('Nome do jogador:'))
gol=str(input('gols do jogador:'))
if gol.isalpha() or gol.isspace():
    gol=0
if nome.isspace() or nome == '' or nome.isnumeric():
    nome = '<desconhecido>'
jogador(gol,nome)