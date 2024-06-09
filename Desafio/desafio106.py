def helpe():
        print('~' * 31)
        print('    SISTEMA DE AJUDA PyHELP')
        print('~' * 31)


while True:
    helpe()
    func=str(input('Funcao ou Biblioteca: '))
    if func=='Fim':
        break
    else:
        help(func)