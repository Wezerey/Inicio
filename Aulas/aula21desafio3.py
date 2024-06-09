def ficha(jog="<desconhecido>", gl=0):
    print(f'O jogador {jog} fez {gl} gol(s) no campeonato')
nome = str(input('Nome do jogador:'))
gol = str(input('Numero de gols'))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gl=gol)
else:
    ficha(nome,gol)