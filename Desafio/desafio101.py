
def voto(i):
    from datetime import datetime
    idade = datetime.now().year - i
    if idade < 16:
        print(f'Com {i} anos: NAO VOTA')
    elif idade <= 65:
        print(f'Com {i} anos: VOTO OBRIGATORIO')
    else:
        print(f'Com {i} anos: VOTO OPCIONAL')


Nascimento = int(input('Nascimento: '))
voto(Nascimento)